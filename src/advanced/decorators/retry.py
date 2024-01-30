"""Retry decorator.

This method is a decorator that retries a function call a number of times, with
a exponential delay between retries.

"""
import logging
from time import sleep
from typing import Callable

logging.basicConfig(name=__name__, format="%(message)s", level=logging.DEBUG)
logger = logging.getLogger(__name__)


def retry(attempts: int = 3, delay: float = 1.0):
    """Retry decorator.

    This method is a decorator that retries a function call a number of times,
    with a exponential delay between retries.
    If max attempts is reached, the exception is raised by the function,
    not captured in logs.

    Args:
        attempts (int): Number of times to retry the operation.
        delay (float): Delay between retries, in seconds.

    Returns:
        (func): Decorated function
    """

    def decorator(func: Callable):
        def wrapper(*args, **kwargs):
            exception = None
            for current_attempt in range(1, attempts + 1):
                try:
                    logger.debug("Attempt %s", current_attempt)
                    return func(*args, **kwargs)
                except Exception as exc:
                    if current_attempt < attempts:
                        logger.warning("Exception, retrying")
                        sleep((1 + delay) ** current_attempt)
                    else:
                        exception = exc
            logger.error("Raising exception, max attempts reached")
            raise exception

        return wrapper

    return decorator
