"""Module to show how to handle exceptions.

This module contains different methods to handle exceptions.

"""

from .custom_exceptions import CustomError  # noqa: F401
from .exceptions import (
    exception_controlled,  # noqa: F401
    exception_controlled_raise_custom_exception,  # noqa: F401
    exception_controlled_raise_exception,  # noqa: F401
    exception_uncontrolled,  # noqa: F401
    exception_with_finally,  # noqa: F401
)
