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
    exception: Exception

    def __init__(self, **kwargs) -> None:
        """Initialize CustomError with message and exception.

        Args:
            **kwargs: Keyword arguments that must include:
                message (str): A descriptive message explaining the error.
                exception (Exception): The original exception being wrapped.

        Raises:
            KeyError: If 'message' or 'exception' keys are not provided
                in kwargs.
        """
        self.message = kwargs["message"]
        self.exception = kwargs["exception"]
