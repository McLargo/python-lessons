"""Module with a sample CustomError class.

This module demonstrates how to create custom exception classes in Python.
Custom exceptions allow you to create specific error types for your application,
making error handling more precise and informative.
"""


class CustomError(Exception):
    """Custom exception class for demonstrating exception handling patterns.

    This class extends the built-in Exception class to create a custom
    exception that can carry additional context about the error, including
    the original exception and a custom message.

    Attributes:
        message: A descriptive message explaining the error context.
        exception: The original exception that triggered this custom error.
    """

    message: str
    exception: Exception | None

    def __init__(
        self,
        message: str,
        exception: Exception | None = None,
    ) -> None:
        """Initialize CustomError with message and exception.

        Args:
            message (str): A descriptive message explaining the error.
            exception (Exception | None): The original exception being wrapped.
                Defaults to None if no exception is being wrapped.
        """
        super().__init__(message)
        self.message = message
        self.exception = exception

    def __str__(self) -> str:
        """Return a string representation of the CustomError."""
        if self.exception:
            return (
                f"{self.message} (caused by "
                f"{type(self.exception).__name__}: {self.exception})"
            )
        return self.message
