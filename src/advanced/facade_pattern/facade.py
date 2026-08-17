"""Facade method pattern example in Python.

This module demonstrates the Facade pattern through a simple bookstore system.
It provides simple interfaces to manage and list books, abstracting away the
complexities of the underlying subsystems (such as databases, external APIs,
etc.).

"""

ISBN10_LENGTH = 10
ISBN13_LENGTH = 13


class Book:
    """Represents a book in the bookstore.

    Attributes:
        isbn: The International Standard Book Number of the book.
        title: The title of the book.
        author: The author of the book.
    """

    def __init__(self, isbn: str, title: str, author: str) -> None:
        """Initialize a Book instance.

        Args:
            isbn: The International Standard Book Number of the book.
            title: The title of the book.
            author: The author of the book.
        """
        self.isbn = isbn
        self.title = title
        self.author = author


class BookManager:
    """Manages a collection of books in the bookstore.

    For this example, it uses an in-memory list to store books. In a real-world,
    it could be any database.
    """

    def __init__(self) -> None:
        """Initialize the BookManager with an empty list of books."""
        self.books: list[Book] = []

    def add_book(self, book: Book) -> None:
        """Add a book to the collection.

        Args:
            book: The Book instance to be added.
        """
        self.books.append(book)

    def list_books(self) -> list[Book]:
        """List all books in the collection.

        Returns:
            A list of Book instances.
        """
        return self.books

    def find_book_by_isbn(self, isbn: str) -> Book | None:
        """Find a book by its ISBN.

        Args:
            isbn: The International Standard Book Number of the book to find.

        Returns:
            The Book instance if found, otherwise None.
        """
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def remove_book(self, isbn: str) -> bool:
        """Remove a book from the collection by its ISBN.

        Args:
            isbn: The International Standard Book Number of the book to remove.

        Returns:
            True if the book was removed, False otherwise.
        """
        book = self.find_book_by_isbn(isbn)
        if book:
            self.books.remove(book)
            return True
        return False


class InventoryBookStock:
    """Manages the stock levels of books in the bookstore.

    In this example, it uses an in-memory dictionary to track stock levels. In a
    real-world, it could be a external inventory management system.
    """

    def __init__(self) -> None:
        """Initialize the InventoryBookStock with an empty stock dictionary."""
        self.stock: dict[str, int] = {}

    def set_stock(self, isbn: str, quantity: int) -> None:
        """Set the stock level for a specific book.

        Args:
            isbn: The International Standard Book Number of the book.
            quantity: The stock level to set for the book.
        """
        self.stock[isbn] = quantity

    def get_stock(self, isbn: str) -> int:
        """Get the stock level for a specific book.

        Args:
            isbn: The International Standard Book Number of the book.

        Returns:
            The stock level of the book. Returns 0 if the book is not found.
        """
        return self.stock.get(isbn, 0)

    def purchase_book(self, isbn: str, quantity: int) -> bool:
        """Purchase a specific quantity of a book.

        Args:
            isbn: The International Standard Book Number of the book.
            quantity: The quantity to purchase.

        Returns:
            True if the purchase was successful (enough stock), False otherwise.
        """
        current_stock = self.get_stock(isbn)
        if current_stock >= quantity:
            self.stock[isbn] = current_stock - quantity
            return True
        return False


class IsbnValidator:
    """Validates ISBN numbers for books.

    This class provides methods to validate the format of both ISBN-10 and
    ISBN-13. In a real-world scenario this could be delegated to an external
    service.
    """

    @staticmethod
    def is_valid_isbn(isbn: str) -> bool:
        """Validate the given ISBN number (ISBN-10 or ISBN-13).

        Hyphens and spaces are ignored. The check digit is verified against
        the standard checksum for the detected format.

        Args:
            isbn: The International Standard Book Number to validate.

        Returns:
            True if the ISBN is a valid ISBN-10 or ISBN-13, False otherwise.
        """
        if not isbn:
            return False

        normalized = isbn.replace("-", "").replace(" ", "")

        if len(normalized) == ISBN10_LENGTH:
            return IsbnValidator._is_valid_isbn10(normalized)
        if len(normalized) == ISBN13_LENGTH:
            return IsbnValidator._is_valid_isbn13(normalized)
        return False

    @staticmethod
    def _is_valid_isbn10(isbn: str) -> bool:
        """Validate a normalized 10-character ISBN-10 string.

        Args:
            isbn: The normalized ISBN-10 string (no hyphens or spaces).

        Returns:
            True if the checksum is valid, False otherwise.
        """
        if not isbn[:-1].isdigit() or isbn[-1] not in "0123456789X":
            return False
        total = sum(
            (i + 1) * (10 if x == "X" else int(x)) for i, x in enumerate(isbn)
        )
        return total % 11 == 0

    @staticmethod
    def _is_valid_isbn13(isbn: str) -> bool:
        """Validate a normalized 13-character ISBN-13 string.

        Args:
            isbn: The normalized ISBN-13 string (no hyphens or spaces).

        Returns:
            True if the checksum is valid, False otherwise.
        """
        if not isbn.isdigit():
            return False
        total = sum(
            int(x) * (1 if i % 2 == 0 else 3) for i, x in enumerate(isbn)
        )
        return total % 10 == 0


class BookstoreFacade:
    """Facade for managing books and their stock in the bookstore."""

    def __init__(
        self,
        book_manager: BookManager,
        inventory_stock: InventoryBookStock,
        isbn_validator: IsbnValidator,
    ) -> None:
        """Initialize the BookstoreFacade with its subsystem collaborators.

        Args:
            book_manager: Subsystem responsible for storing and retrieving
                books.
            inventory_stock: Subsystem responsible for tracking stock levels.
            isbn_validator: Subsystem responsible for validating ISBN numbers.
        """
        self.book_manager = book_manager
        self.inventory_stock = inventory_stock
        self.isbn_validator = isbn_validator

    @classmethod
    def create(cls) -> "BookstoreFacade":
        """Create a facade instance with default subsystem collaborators.

        Convenience factory that wires up fresh instances of every subsystem
        used by the facade. Prefer the regular constructor when you need to
        inject custom or pre-configured subsystems (e.g. in tests).

        Returns:
            A new BookstoreFacade backed by default subsystem instances.
        """
        book_manager = BookManager()
        inventory_stock = InventoryBookStock()
        isbn_validator = IsbnValidator()
        return cls(
            book_manager=book_manager,
            inventory_stock=inventory_stock,
            isbn_validator=isbn_validator,
        )

    def new_book(
        self,
        isbn: str,
        title: str,
        author: str,
        quantity: int,
    ) -> None:
        """Add a book to the bookstore and set its stock level.

        Args:
            isbn: The International Standard Book Number of the book.
            title: The title of the book.
            author: The author of the book.
            quantity: The stock level to set for the book.

        Raises:
            ValueError: If isbn is not a valid ISBN-10 or ISBN-13.
        """
        if not self.isbn_validator.is_valid_isbn(isbn):
            raise ValueError(f"Invalid ISBN: {isbn}")

        book = Book(isbn, title, author)
        self.book_manager.add_book(book)
        self.inventory_stock.set_stock(isbn, quantity)

    def list_books_with_stock(self) -> list[str]:
        """List all books in the bookstore with stock.

        Returns:
            A list of books that have stock available.
        """
        books = self.book_manager.list_books()
        books_with_stock = []
        for book in books:
            if self.inventory_stock.get_stock(book.isbn) > 0:
                books_with_stock.append(book.title)

        return books_with_stock

    def purchase_book(self, isbn: str, quantity: int) -> bool:
        """Purchase a specific quantity of a book.

        Args:
            isbn: The International Standard Book Number of the book.
            quantity: The quantity to purchase.

        Returns:
            True if the purchase was successful (enough stock), False otherwise.
        """
        if self.book_manager.find_book_by_isbn(isbn):
            return self.inventory_stock.purchase_book(isbn, quantity)
        return False
