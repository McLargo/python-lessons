"""Module with a sample CustomError class.

This class is just an example of a CustomError class.

"""


class CustomError(Exception):
    """Custom error class."""

    message = str
    exception = Exception

    def __init__(self, **kwargs):
        """Init CustomError exception."""
        self.message = kwargs["message"]
        self.exception = kwargs["exception"]
