"""Module to show how to handle exceptions.

This module contains different methods to handle exceptions.

"""

import logging

from .custom_exceptions import CustomError

logging.basicConfig(name=__name__, format="%(message)s", level=logging.DEBUG)
logger = logging.getLogger(__name__)


def exception_uncontrolled() -> None:
    """Method that raises an exception that is not handled correctly.

    Raises:
        TypeError: cannot sum int&string types
    """
    number = 1
    char = "a"
    number + char  # raise TypeError, cannot sum int&string types


def exception_controlled() -> None:
    """Method that control the exception, no raise."""
    number = 1
    char = "a"
    try:
        number + char  # raise TypeError, cannot sum int&string types
    except TypeError:
        logger.warning("Cannot sum int + string. Continue.")
        pass


def exception_controlled_raise_exception() -> None:
    """Method that control the exception, raising the same exception.

    Raises:
        TypeError: cannot sum int&string types
    """
    number = 1
    char = "a"
    try:
        number + char  # raise TypeError, cannot sum int&string types
    except TypeError as exc:
        logger.error("Cannot sum int + string. Raising TypeError.")
        raise exc


def exception_controlled_raise_custom_exception() -> None:
    """Method that control the exception, raising custom exception.

    Raises:
        TypeError: cannot sum int&string types
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
        )


def exception_with_finally(raise_exception: bool) -> None:
    """Method that control the exception, raising custom exception.

    Arguments:
        raise_exception (bool): flag to raise exception or not

    Raises:
        TypeError: cannot sum int&string types
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
