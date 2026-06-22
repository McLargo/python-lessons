"""Module to show how to handle exceptions.

This module contains different methods to handle exceptions.

"""

import logging

from .custom_exceptions import CustomError

logging.basicConfig(format="%(message)s", level=logging.DEBUG)
logger = logging.getLogger(__name__)


def exception_uncontrolled() -> None:
    """Example of an unhandled exception that propagates to the caller.

    This function intentionally performs an invalid operation (adding an
    integer and a string) without catching the exception. This shows what
    happens when exceptions are not handled - they propagate up the call
    stack until caught or the program crashes.

    Raises:
        TypeError: When attempting to add incompatible types (int + str).
    """
    number = 1
    char = "a"
    number + char  # raise TypeError, cannot sum int&string types


def exception_controlled() -> None:
    """Example of proper exception handling by catching and logging.

    This function shows how to catch an exception, log it, and continue
    execution gracefully. This is appropriate when the error is expected
    and recoverable, and you want the program to continue running.
    """
    number = 1
    char = "a"
    try:
        number + char  # raise TypeError, cannot sum int&string types
    except TypeError:
        logger.warning("Cannot sum int + string. Continue.")
        pass


def exception_controlled_raise_exception() -> None:
    """Example of catching and re-raising the same exception.

    This function shows how to catch an exception, log relevant information,
    and then re-raise the same exception. This pattern is useful when you
    want to add logging or perform cleanup while still propagating the
    error to the caller.

    Raises:
        TypeError: When attempting to add incompatible types (int + str).
    """
    number = 1
    char = "a"
    try:
        number + char  # raise TypeError, cannot sum int&string types
    except TypeError as exc:
        logger.error("Cannot sum int + string. Raising TypeError.")
        raise exc


def exception_controlled_raise_custom_exception() -> None:
    """Example of catching and raising a custom exception.

    This function shows how to catch a built-in exception and raise a
    custom exception instead. This pattern is useful for wrapping
    low-level exceptions with domain-specific errors that provide
    better context to callers.

    Raises:
        CustomError: A custom exception wrapping the original TypeError.
    """
    number = 1
    char = "a"
    try:
        number + char  # raise TypeError, cannot sum int&string types
    except TypeError as exc:
        logger.error("Cannot sum int + string. Raising CustomError.")
        raise CustomError(
            message="Controlled TypeError",
            exception=exc,
        ) from exc


def exception_with_finally(raise_exception: bool) -> None:
    """Example of using finally clause for cleanup code.

    This function shows how the finally block executes regardless of
    whether an exception is raised or not. The finally block is useful
    for cleanup operations that must always run, such as closing files
    or releasing resources.

    Args:
        raise_exception: If True, raises a TypeError. If False, executes
            successfully without raising an exception.

    Raises:
        TypeError: When raise_exception is True and attempting to add
            incompatible types (int + str).
    """
    number = 1
    char = "a"
    try:
        if raise_exception:
            number + char  # raise TypeError, cannot sum int&string types
        else:
            number + 10
    except TypeError as exc:
        logger.error("Cannot sum int + string. Raising TypeError.")
        raise exc
    finally:
        logger.debug("Finally is executed.")
