"""Chain of Responsibility pattern example in Python."""

from abc import ABC, abstractmethod
from typing import Optional


class Handler(ABC):
    """Abstract base class for handlers in the chain of responsibility.

    This class defines the interface that all concrete handlers must implement.
    Each handler has a reference to the next handler in the chain.
    """

    def __init__(self, next: Optional["Handler"] = None) -> None:
        """Initialize the handler with an optional next handler.

        Args:
            next: The next handler in the chain. If None, this is the last
                handler in the chain. Defaults to None.
        """
        self.next = next

    @abstractmethod
    def handle(self, line: str) -> None:
        """Handle the line or pass it to the successor.

        Args:
            line: The line to be handled.

        Raises:
            NotImplementedError: Must be implemented by concrete handlers.
        """
        pass


class LengthValidationHandler(Handler):
    """Concrete handler for line length validation.

    Validates that the line does not exceed a maximum length.
    If the line is valid, passes it to the next handler in the chain.
    """

    MAX_LENGTH = 80

    def handle(self, line: str) -> None:
        """Validate line length and pass to the next handler.

        Args:
            line: The line to be validated.

        Raises:
            ValueError: If the line length exceeds MAX_LENGTH characters.
        """
        if len(line) > self.MAX_LENGTH:
            raise ValueError(
                f"Line length exceeds {self.MAX_LENGTH} characters.",
            )
        if self.next:
            self.next.handle(line)


class PrefixValidationHandler(Handler):
    """Concrete handler for line prefix validation.

    Validates that the line starts with a specific prefix.
    If the line is valid, passes it to the next handler in the chain.
    """

    PREFIX = "INFO"

    def handle(self, line: str) -> None:
        """Validate line prefix and pass to the next handler.

        Args:
            line: The line to be validated.

        Raises:
            ValueError: If the line does not start with PREFIX.
        """
        if not line.startswith(self.PREFIX):
            raise ValueError(f"Line does not start with '{self.PREFIX}'.")
        if self.next:
            self.next.handle(line)


class SuffixValidationHandler(Handler):
    """Concrete handler for line suffix validation.

    Validates that the line ends with a specific suffix.
    If the line is valid, passes it to the next handler in the chain.
    """

    SUFFIX = "END"

    def handle(self, line: str) -> None:
        """Validate line suffix and pass to the next handler.

        Args:
            line: The line to be validated.

        Raises:
            ValueError: If the line does not end with SUFFIX.
        """
        if not line.endswith(self.SUFFIX):
            raise ValueError(f"Line does not end with '{self.SUFFIX}'.")
        if self.next:
            self.next.handle(line)


class ContentValidationHandler(Handler):
    """Concrete handler for line content validation.

    Validates that the line contains exactly the required number of
    parts separated by a specific separator.
    If the line is valid, passes it to the next handler in the chain.
    """

    SEPARATOR = "|"
    TOTAL_PARTS = 5

    def handle(self, line: str) -> None:
        """Validate line content structure and pass to the next handler.

        Args:
            line: The line to be validated.

        Raises:
            ValueError: If the line does not contain exactly TOTAL_PARTS
                parts separated by SEPARATOR.
        """
        parts = line.split(self.SEPARATOR)
        if len(parts) != self.TOTAL_PARTS:
            raise ValueError(
                f"Line does not contain {self.TOTAL_PARTS} parts "
                f"separated by '{self.SEPARATOR}'.",
            )
        if self.next:
            self.next.handle(line)


class ChainOfResponsibility:
    """Class to manage the chain of responsibility.

    This class initializes and manages a chain of validation handlers.
    The chain processes lines in the following order:
    1. Length validation
    2. Prefix validation
    3. Suffix validation
    4. Content structure validation
    """

    def __init__(self) -> None:
        """Initialize the chain with all validation handlers in order."""
        self.chain = LengthValidationHandler(
            PrefixValidationHandler(
                SuffixValidationHandler(
                    ContentValidationHandler(),
                ),
            ),
        )

    def process(self, line: str) -> None:
        """Process the line through the entire validation chain.

        Args:
            line: The line to be processed and validated.

        Raises:
            ValueError: If any validation in the chain fails.
        """
        self.chain.handle(line)
