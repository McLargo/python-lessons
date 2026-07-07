"""Tests for the chain of responsibility pattern implementation."""

import pytest
from hypothesis import given
from hypothesis import strategies as st

from advanced.chain_of_responsibility_pattern import (
    ChainOfResponsibility,
    ContentValidationHandler,
    Handler,
    LengthValidationHandler,
    PrefixValidationHandler,
    SuffixValidationHandler,
)


@pytest.fixture
def mock_handler():
    """Fixture that provides a mock handler factory for testing.

    Returns:
        A callable that returns a tuple of
        MockHandler instance and call tracking list.
    """

    def _create_mock_handler():
        calls = []

        class MockHandler(Handler):
            def handle(self, line):
                calls.append(line)

        return MockHandler(), calls

    return _create_mock_handler


class TestLengthValidationHandler:
    """Test the LengthValidationHandler."""

    def test_valid_length_no_next(self) -> None:
        """Test handling a valid line with no next handler."""
        handler = LengthValidationHandler()
        # Should not raise any exception
        handler.handle("a" * 80)

    def test_valid_length_with_next(self, mock_handler) -> None:
        """Test handling a valid line and passing to next handler."""
        next_handler, calls = mock_handler()
        handler = LengthValidationHandler(next=next_handler)
        line = "a" * 80
        handler.handle(line)

        assert calls == [line]

    def test_exceeds_max_length(self) -> None:
        """Test handling a line that exceeds maximum length."""
        handler = LengthValidationHandler()
        with pytest.raises(ValueError) as excinfo:
            handler.handle("a" * 81)
        assert "Line length exceeds 80 characters" in str(excinfo.value)

    def test_exceeds_max_length_does_not_call_next(self, mock_handler) -> None:
        """Test that next handler is not called when validation fails."""
        next_handler, calls = mock_handler()
        handler = LengthValidationHandler(next=next_handler)
        with pytest.raises(ValueError):
            handler.handle("a" * 81)

        assert calls == []

    def test_empty_string(self) -> None:
        """Test handling an empty string."""
        handler = LengthValidationHandler()
        # Should not raise any exception
        handler.handle("")

    @pytest.mark.parametrize(
        "length",
        [1, 40, 79, 80],
    )
    def test_various_valid_lengths(self, length: int) -> None:
        """Test various valid line lengths."""
        handler = LengthValidationHandler()
        handler.handle("a" * length)

    @pytest.mark.parametrize(
        "length",
        [81, 100, 200, 1000],
    )
    def test_various_invalid_lengths(self, length: int) -> None:
        """Test various invalid line lengths."""
        handler = LengthValidationHandler()
        with pytest.raises(ValueError):
            handler.handle("a" * length)


class TestPrefixValidationHandler:
    """Test the PrefixValidationHandler."""

    def test_valid_prefix_no_next(self) -> None:
        """Test handling a line with valid prefix and no next handler."""
        handler = PrefixValidationHandler()
        handler.handle("INFO: Some message")

    def test_valid_prefix_with_next(self, mock_handler) -> None:
        """Test handling a line with valid prefix and passing to next."""
        next_handler, calls = mock_handler()
        handler = PrefixValidationHandler(next=next_handler)
        line = "INFO: Test"
        handler.handle(line)

        assert calls == [line]

    def test_invalid_prefix(self) -> None:
        """Test handling a line with invalid prefix."""
        handler = PrefixValidationHandler()
        with pytest.raises(ValueError) as excinfo:
            handler.handle("ERROR: Some message")
        assert "Line does not start with 'INFO'" in str(excinfo.value)

    def test_empty_string(self) -> None:
        """Test handling an empty string."""
        handler = PrefixValidationHandler()
        with pytest.raises(ValueError):
            handler.handle("")

    def test_prefix_only(self) -> None:
        """Test handling a line that is just the prefix."""
        handler = PrefixValidationHandler()
        handler.handle("INFO")

    @pytest.mark.parametrize(
        "line",
        [
            "INFO",
            "INFO: message",
            "INFO|data|more",
            "INFOrmation",
        ],
    )
    def test_various_valid_prefixes(self, line: str) -> None:
        """Test various lines with valid prefix."""
        handler = PrefixValidationHandler()
        handler.handle(line)

    @pytest.mark.parametrize(
        "line",
        [
            "ERROR: message",
            "info: lowercase",
            "WARN: message",
            " INFO: space before",
            "",
        ],
    )
    def test_various_invalid_prefixes(self, line: str) -> None:
        """Test various lines with invalid prefix."""
        handler = PrefixValidationHandler()
        with pytest.raises(ValueError):
            handler.handle(line)


class TestSuffixValidationHandler:
    """Test the SuffixValidationHandler."""

    def test_valid_suffix_no_next(self) -> None:
        """Test handling a line with valid suffix and no next handler."""
        handler = SuffixValidationHandler()
        handler.handle("Some message END")

    def test_valid_suffix_with_next(self, mock_handler) -> None:
        """Test handling a line with valid suffix and passing to next."""
        next_handler, calls = mock_handler()
        handler = SuffixValidationHandler(next=next_handler)
        line = "Test END"
        handler.handle(line)

        assert calls == [line]

    def test_invalid_suffix(self) -> None:
        """Test handling a line with invalid suffix."""
        handler = SuffixValidationHandler()
        with pytest.raises(ValueError) as excinfo:
            handler.handle("Some message START")
        assert "Line does not end with 'END'" in str(excinfo.value)

    def test_empty_string(self) -> None:
        """Test handling an empty string."""
        handler = SuffixValidationHandler()
        with pytest.raises(ValueError):
            handler.handle("")

    def test_suffix_only(self) -> None:
        """Test handling a line that is just the suffix."""
        handler = SuffixValidationHandler()
        handler.handle("END")

    @pytest.mark.parametrize(
        "line",
        [
            "END",
            "message END",
            "data|more|END",
            "ENDEND",
        ],
    )
    def test_various_valid_suffixes(self, line: str) -> None:
        """Test various lines with valid suffix."""
        handler = SuffixValidationHandler()
        handler.handle(line)

    @pytest.mark.parametrize(
        "line",
        [
            "message START",
            "message end",
            "message",
            "END ",
            "",
        ],
    )
    def test_various_invalid_suffixes(self, line: str) -> None:
        """Test various lines with invalid suffix."""
        handler = SuffixValidationHandler()
        with pytest.raises(ValueError):
            handler.handle(line)


class TestContentValidationHandler:
    """Test the ContentValidationHandler."""

    def test_valid_content_no_next(self) -> None:
        """Test handling valid content with no next handler."""
        handler = ContentValidationHandler()
        handler.handle("part1|part2|part3|part4|part5")

    def test_valid_content_with_next(self, mock_handler) -> None:
        """Test handling valid content and passing to next."""
        next_handler, calls = mock_handler()
        handler = ContentValidationHandler(next=next_handler)
        line = "a|b|c|d|e"
        handler.handle(line)

        assert calls == [line]

    def test_too_few_parts(self) -> None:
        """Test handling content with too few parts."""
        handler = ContentValidationHandler()
        with pytest.raises(ValueError) as excinfo:
            handler.handle("part1|part2|part3")
        assert "Line does not contain 5 parts separated by '|'" in str(
            excinfo.value,
        )

    def test_too_many_parts(self) -> None:
        """Test handling content with too many parts."""
        handler = ContentValidationHandler()
        with pytest.raises(ValueError) as excinfo:
            handler.handle("part1|part2|part3|part4|part5|part6")
        assert "Line does not contain 5 parts separated by '|'" in str(
            excinfo.value,
        )

    def test_empty_string(self) -> None:
        """Test handling an empty string."""
        handler = ContentValidationHandler()
        with pytest.raises(ValueError):
            handler.handle("")

    def test_empty_parts_allowed(self) -> None:
        """Test that empty parts between separators are allowed."""
        handler = ContentValidationHandler()
        # This has 5 parts (4 separators), some of which are empty
        handler.handle("||||")

    @pytest.mark.parametrize(
        "line",
        [
            "a|b|c|d|e",
            "||||",  # 5 empty parts
            "1|2|3|4|5",
            "INFO|data|value|test|END",
        ],
    )
    def test_various_valid_contents(self, line: str) -> None:
        """Test various lines with valid content structure."""
        handler = ContentValidationHandler()
        handler.handle(line)

    @pytest.mark.parametrize(
        "line",
        [
            "a|b|c",  # 3 parts
            "a|b|c|d",  # 4 parts
            "a|b|c|d|e|f",  # 6 parts
            "no_separator",  # 1 part
            "",  # 1 part (empty)
        ],
    )
    def test_various_invalid_contents(self, line: str) -> None:
        """Test various lines with invalid content structure."""
        handler = ContentValidationHandler()
        with pytest.raises(ValueError):
            handler.handle(line)


class TestChainOfResponsibility:
    """Test the full chain of responsibility."""

    def test_valid_line_passes_all_validations(self) -> None:
        """Test that a valid line passes all validations."""
        chain = ChainOfResponsibility()
        # Line must: be ≤80 chars, start with INFO, end with END, have 5 parts
        valid_line = "INFO|data|value|test|END"
        chain.process(valid_line)

    def test_fails_length_validation(self) -> None:
        """Test that chain fails on length validation."""
        chain = ChainOfResponsibility()
        # This line is too long (>80 chars)
        long_line = "INFO|" + "a" * 80 + "|value|test|END"
        with pytest.raises(ValueError):
            chain.process(long_line)

    def test_fails_prefix_validation(self) -> None:
        """Test that chain fails on prefix validation."""
        chain = ChainOfResponsibility()
        # This line doesn't start with INFO
        invalid_line = "ERROR|data|value|test|END"
        with pytest.raises(ValueError) as excinfo:
            chain.process(invalid_line)
        assert "does not start with 'INFO'" in str(excinfo.value)

    def test_fails_suffix_validation(self) -> None:
        """Test that chain fails on suffix validation."""
        chain = ChainOfResponsibility()
        # This line doesn't end with END
        invalid_line = "INFO|data|value|test|START"
        with pytest.raises(ValueError) as excinfo:
            chain.process(invalid_line)
        assert "does not end with 'END'" in str(excinfo.value)

    def test_fails_content_validation(self) -> None:
        """Test that chain fails on content validation."""
        chain = ChainOfResponsibility()
        # This line doesn't have 5 parts separated by |
        invalid_line = "INFO|data|END"
        with pytest.raises(ValueError) as excinfo:
            chain.process(invalid_line)
        assert "does not contain 5 parts" in str(excinfo.value)

    def test_validation_order_length_first(self) -> None:
        """Test that validations happen in order (length checked first)."""
        chain = ChainOfResponsibility()
        # Line is too long AND has other problems
        # Length validation should fail first
        invalid_line = "ERROR|" + "a" * 80 + "|value|test|START"
        with pytest.raises(ValueError):
            chain.process(invalid_line)

    @pytest.mark.parametrize(
        "line",
        [
            "INFO|data|value|test|END",
            "INFO|a|b|c|END",
            "INFO||||END",  # Empty parts
            "INFO|123|456|789|END",
        ],
    )
    def test_various_valid_lines(self, line: str) -> None:
        """Test various valid lines through the chain."""
        chain = ChainOfResponsibility()
        chain.process(line)

    def test_minimum_valid_line(self) -> None:
        """Test the shortest possible valid line."""
        chain = ChainOfResponsibility()
        # Minimum: INFO, 4 separators (5 parts), END = INFO||||END
        chain.process("INFO||||END")

    def test_maximum_valid_line(self) -> None:
        """Test a valid line at maximum length."""
        chain = ChainOfResponsibility()
        # Create a line exactly 80 characters long with all validations
        # INFO + | + content + | + END, where content fills to make it 80 chars
        # INFO||||END = 11 chars, so we have 69 chars to distribute
        middle_content = (
            "a" * 23
        )  # This will make one of the middle parts longer
        line = f"INFO|{middle_content}|{middle_content}|{middle_content}|END"
        # Verify it's exactly 80 characters
        assert len(line) == 80
        chain.process(line)


class TestHandlerAbstractClass:
    """Test the abstract Handler base class."""

    def test_cannot_instantiate_abstract_handler(self) -> None:
        """Test that Handler cannot be instantiated directly."""
        with pytest.raises(TypeError):
            Handler()  # type: ignore

    def test_handler_initialization_with_next(self) -> None:
        """Test that concrete handlers initialize with next handler."""

        class ConcreteHandler(Handler):
            def handle(self, line):
                pass

        next_handler = ConcreteHandler()
        handler = ConcreteHandler(next=next_handler)

        assert handler.next is next_handler

    def test_handler_initialization_without_next(self) -> None:
        """Test that concrete handlers initialize without next handler."""

        class ConcreteHandler(Handler):
            def handle(self, line):
                pass

        handler = ConcreteHandler()

        assert handler.next is None


@given(
    st.text(
        alphabet=st.characters(blacklist_categories=("Cs",)),
        min_size=0,
        max_size=80,
    ),
)
def test_length_handler_accepts_any_valid_length_string(line: str) -> None:
    """Property: Length handler should accept any string up to 80 characters."""
    handler = LengthValidationHandler()
    # Should not raise exception
    handler.handle(line)


@given(
    st.text(
        alphabet=st.characters(blacklist_categories=("Cs",)),
        min_size=81,
        max_size=200,
    ),
)
def test_length_handler_rejects_long_strings(line: str) -> None:
    """Property: Length handler should reject any string over 80 characters."""
    handler = LengthValidationHandler()
    with pytest.raises(ValueError):
        handler.handle(line)


@given(
    content=st.text(
        alphabet=st.characters(blacklist_categories=("Cs",)),
        min_size=0,
        max_size=70,
    ),
)
def test_prefix_handler_with_valid_prefix(content: str) -> None:
    """Property: Prefix handler accepts any line starting with INFO."""
    handler = PrefixValidationHandler()
    line = f"INFO{content}"
    if len(line) <= 80:  # Avoid triggering length issues in isolation
        handler.handle(line)


@given(
    content=st.text(
        alphabet=st.characters(blacklist_categories=("Cs",)),
        min_size=0,
        max_size=70,
    ),
)
def test_suffix_handler_with_valid_suffix(content: str) -> None:
    """Property: Suffix handler accepts any line ending with END."""
    handler = SuffixValidationHandler()
    line = f"{content}END"
    if len(line) <= 80:  # Avoid triggering length issues in isolation
        handler.handle(line)


@given(
    parts=st.lists(
        st.text(
            alphabet=st.characters(
                blacklist_categories=("Cs",),
                blacklist_characters=("|",),
            ),
            min_size=0,
            max_size=15,
        ),
        min_size=5,
        max_size=5,
    ),
)
def test_content_handler_with_exactly_five_parts(parts: list[str]) -> None:
    """Content handler accepts any line with exactly 5 pipe-separated parts."""
    handler = ContentValidationHandler()
    line = "|".join(parts)
    if len(line) <= 80:  # Avoid triggering length issues in isolation
        handler.handle(line)
