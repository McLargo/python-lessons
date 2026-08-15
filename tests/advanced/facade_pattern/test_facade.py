"""Tests for the facade pattern implementation."""

import pytest
from hypothesis import given
from hypothesis import strategies as st

from advanced.facade_pattern import (
    Book,
    BookManager,
    BookstoreFacade,
    InventoryBookStock,
    IsbnValidator,
)

# Known-valid ISBNs used across the tests.
VALID_ISBN10 = "0-306-40615-2"
VALID_ISBN10_WITH_X = "043942089X"
VALID_ISBN13 = "978-0-306-40615-7"


class TestBook:
    """Test cases for the Book value object."""

    def test_book_stores_its_attributes(self) -> None:
        """Book should expose the constructor arguments as attributes."""
        book = Book("123", "Title", "Author")

        assert book.isbn == "123"
        assert book.title == "Title"
        assert book.author == "Author"


class TestBookManager:
    """Test cases for the BookManager subsystem."""

    def test_new_manager_has_no_books(self) -> None:
        """A fresh BookManager should start with an empty catalog."""
        manager = BookManager()

        assert manager.list_books() == []

    def test_add_book_appends_to_catalog(self) -> None:
        """add_book should store the book in the catalog."""
        manager = BookManager()
        book = Book("1", "T", "A")

        manager.add_book(book)

        assert manager.list_books() == [book]

    def test_find_book_by_isbn_returns_matching_book(self) -> None:
        """find_book_by_isbn returns the book with the matching ISBN."""
        manager = BookManager()
        book = Book("1", "T", "A")
        manager.add_book(book)

        assert manager.find_book_by_isbn("1") is book

    def test_find_book_by_isbn_returns_none_when_missing(self) -> None:
        """find_book_by_isbn returns None when nothing matches."""
        manager = BookManager()

        assert manager.find_book_by_isbn("missing") is None

    def test_remove_book_returns_true_and_removes_book(self) -> None:
        """remove_book removes the book and returns True on success."""
        manager = BookManager()
        book = Book("1", "T", "A")
        manager.add_book(book)

        removed = manager.remove_book("1")

        assert removed is True
        assert manager.list_books() == []

    def test_remove_book_returns_false_when_missing(self) -> None:
        """remove_book returns False when the ISBN is not present."""
        manager = BookManager()

        assert manager.remove_book("missing") is False


class TestInventoryBookStock:
    """Test cases for the InventoryBookStock subsystem."""

    def test_get_stock_defaults_to_zero(self) -> None:
        """Unknown ISBNs report a stock level of 0."""
        inventory = InventoryBookStock()

        assert inventory.get_stock("missing") == 0

    def test_set_stock_and_get_stock_roundtrip(self) -> None:
        """set_stock stores the level returned by get_stock."""
        inventory = InventoryBookStock()

        inventory.set_stock("1", 5)

        assert inventory.get_stock("1") == 5

    def test_purchase_book_succeeds_when_stock_is_sufficient(self) -> None:
        """purchase_book returns True and reduces the stock level."""
        inventory = InventoryBookStock()
        inventory.set_stock("1", 5)

        result = inventory.purchase_book("1", 3)

        assert result is True
        assert inventory.get_stock("1") == 2

    def test_purchase_book_succeeds_when_stock_matches_exactly(self) -> None:
        """Buying exactly the available stock is allowed."""
        inventory = InventoryBookStock()
        inventory.set_stock("1", 3)

        result = inventory.purchase_book("1", 3)

        assert result is True
        assert inventory.get_stock("1") == 0

    def test_purchase_book_fails_when_stock_is_insufficient(self) -> None:
        """purchase_book returns False and keeps the stock unchanged."""
        inventory = InventoryBookStock()
        inventory.set_stock("1", 1)

        result = inventory.purchase_book("1", 5)

        assert result is False
        assert inventory.get_stock("1") == 1

    def test_purchase_book_fails_when_book_is_unknown(self) -> None:
        """Purchasing an unknown ISBN returns False."""
        inventory = InventoryBookStock()

        assert inventory.purchase_book("missing", 1) is False


class TestIsbnValidator:
    """Test cases for the IsbnValidator subsystem."""

    @pytest.mark.parametrize(
        "isbn",
        [
            VALID_ISBN10,
            VALID_ISBN10.replace("-", ""),
            "0 306 40615 2",
            VALID_ISBN10_WITH_X,
            VALID_ISBN13,
            VALID_ISBN13.replace("-", ""),
        ],
    )
    def test_valid_isbn_are_accepted(self, isbn: str) -> None:
        """Known-valid ISBN-10 and ISBN-13 values should pass validation."""
        assert IsbnValidator.is_valid_isbn(isbn) is True

    @pytest.mark.parametrize(
        "isbn",
        [
            "",
            "123",
            "1234567890",  # ISBN-10 length but bad checksum
            "0-306-40615-3",  # ISBN-10 with wrong check digit
            "12345Y7890",  # non-digit / non-X character
            "978-0-306-40615-8",  # ISBN-13 with wrong check digit
            "97803064061A7",  # ISBN-13 length with non-digit
            "12345678901234",  # length matches neither format
        ],
    )
    def test_invalid_isbn_are_rejected(self, isbn: str) -> None:
        """Malformed or wrong-checksum ISBNs should fail validation."""
        assert IsbnValidator.is_valid_isbn(isbn) is False


class TestBookstoreFacade:
    """Test cases for the BookstoreFacade."""

    def test_create_wires_default_subsystems(self) -> None:
        """create() returns a facade backed by default subsystem instances."""
        facade = BookstoreFacade.create()

        assert isinstance(facade.book_manager, BookManager)
        assert isinstance(facade.inventory_stock, InventoryBookStock)
        assert isinstance(facade.isbn_validator, IsbnValidator)

    def test_new_book_registers_book_and_stock(self) -> None:
        """new_book stores the book and initializes its stock."""
        facade = BookstoreFacade.create()

        facade.new_book(VALID_ISBN13, "Title", "Author", 4)

        [book] = facade.book_manager.list_books()
        assert book.title == "Title"
        assert book.author == "Author"
        assert book.isbn == VALID_ISBN13
        assert facade.inventory_stock.get_stock(VALID_ISBN13) == 4

    def test_new_book_rejects_invalid_isbn(self) -> None:
        """new_book raises ValueError for invalid ISBNs."""
        facade = BookstoreFacade.create()

        with pytest.raises(ValueError, match="Invalid ISBN"):
            facade.new_book("not-an-isbn", "T", "A", 1)

        assert facade.book_manager.list_books() == []
        assert facade.inventory_stock.get_stock("not-an-isbn") == 0

    def test_list_books_with_stock_filters_out_empty_stock(self) -> None:
        """Only titles of books with a positive stock level are returned."""
        facade = BookstoreFacade.create()
        facade.new_book(VALID_ISBN13, "In stock", "A", 2)
        facade.new_book(VALID_ISBN10, "Out of stock", "B", 0)

        in_stock = facade.list_books_with_stock()

        assert in_stock == ["In stock"]

    def test_purchase_book_decrements_stock_on_success(self) -> None:
        """A successful purchase reduces the stock level."""
        facade = BookstoreFacade.create()
        facade.new_book(VALID_ISBN13, "T", "A", 5)

        assert facade.purchase_book(VALID_ISBN13, 2) is True
        assert facade.inventory_stock.get_stock(VALID_ISBN13) == 3

    def test_purchase_book_fails_when_stock_is_insufficient(self) -> None:
        """A failing purchase returns False and leaves stock untouched."""
        facade = BookstoreFacade.create()
        facade.new_book(VALID_ISBN13, "T", "A", 1)

        assert facade.purchase_book(VALID_ISBN13, 5) is False
        assert facade.inventory_stock.get_stock(VALID_ISBN13) == 1

    def test_purchase_book_fails_when_book_is_unknown(self) -> None:
        """Purchasing a book that was never registered returns False."""
        facade = BookstoreFacade.create()
        facade.inventory_stock.set_stock(VALID_ISBN13, 5)

        assert facade.purchase_book(VALID_ISBN13, 1) is False
        assert facade.inventory_stock.get_stock(VALID_ISBN13) == 5


class TestIsbnValidatorProperties:
    """Property-based tests for the ISBN-13 checksum logic."""

    @staticmethod
    def _isbn13_check_digit(first_twelve: str) -> str:
        """Compute the ISBN-13 check digit for the first twelve digits."""
        total = sum(
            int(d) * (1 if i % 2 == 0 else 3)
            for i, d in enumerate(first_twelve)
        )
        return str((10 - total % 10) % 10)

    @given(st.text(alphabet="0123456789", min_size=12, max_size=12))
    def test_any_prefix_with_correct_check_digit_is_valid(
        self,
        prefix: str,
    ) -> None:
        """Any 12 digits paired with the correct check digit are valid."""
        check = self._isbn13_check_digit(prefix)

        assert IsbnValidator.is_valid_isbn(prefix + check) is True

    @given(
        prefix=st.text(alphabet="0123456789", min_size=12, max_size=12),
        position=st.integers(min_value=0, max_value=12),
        delta=st.integers(min_value=1, max_value=9),
    )
    def test_mutating_any_digit_invalidates_isbn13(
        self,
        prefix: str,
        position: int,
        delta: int,
    ) -> None:
        """Apply any single digit to a different value breaks the checksum."""
        check = self._isbn13_check_digit(prefix)
        original = prefix + check
        mutated_digit = str((int(original[position]) + delta) % 10)
        mutated = original[:position] + mutated_digit + original[position + 1 :]

        assert IsbnValidator.is_valid_isbn(mutated) is False
