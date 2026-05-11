"""Concurrent examples using ThreadPoolExecutor and async functions."""

import asyncio
from concurrent.futures import ThreadPoolExecutor
from time import sleep

from advanced.concurrency_parallelism.utils import (
    PRIMES,
    WORKERS,
    is_prime_with_pid,
)


def concurrent_with_thread_pool() -> list[tuple[int, bool, int]]:
    """Example of ThreadPoolExecutor to check if a number is prime.

    Returns:
        list: List of tuples (number, is_prime_result, process_id)
    """
    with ThreadPoolExecutor(max_workers=WORKERS) as executor:
        return list(executor.map(is_prime_with_pid, PRIMES))


async def async_method_not_blocked():
    """Good usage of async functions.

    The sleep function does not block the event loop.
    """
    await asyncio.sleep(1)


async def async_method_blocked():
    """Bad usage of async functions.

    The sleep function blocks the event loop.
    """
    sleep(1)
