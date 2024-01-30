"""Measure decorator.

This method is a decorator that measures the execution time of a function.

"""
import logging
from time import time
from typing import Callable

logging.basicConfig(name=__name__, format="%(message)s", level=logging.DEBUG)
logger = logging.getLogger(__name__)


def measure(func: Callable):
    """Measure decorator.

    This method is a decorator that measures the execution time in seconds
    of a function.

    Args:
        func (Callable): Function to decorate

    Returns:
        (func): Decorated function
    """

    def wrapper(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        elapsed_sec = time() - start
        elapsed_format = f"{elapsed_sec:.3f}"
        logger.debug(
            "Method %s executed in %s seconds",
            func.__name__,
            elapsed_format,
        )

    return wrapper
