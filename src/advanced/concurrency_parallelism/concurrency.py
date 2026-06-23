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
    """Example of thread-based concurrency for I/O-bound.

    Uses ThreadPoolExecutor to distribute work across multiple threads.

    Returns:
        List of tuples where each tuple contains
        (number, is_prime_result, process_id).
        Note that process_id will be the same for all tuples since threads
        share the same process, unlike multiprocessing which creates
        separate processes.
    """
    with ThreadPoolExecutor(max_workers=WORKERS) as executor:
        return list(executor.map(is_prime_with_pid, PRIMES))


async def async_method_not_blocked() -> None:
    """Example of proper async/await usage without blocking the event loop.

    This function uses asyncio.sleep() which is non-blocking and yields
    control back to the event loop. This allows other async tasks to run
    during the sleep period, making efficient use of the single thread.
    This is the correct pattern for async functions.

    Returns:
        None. This is a coroutine that must be awaited.
    """
    await asyncio.sleep(1)


async def async_method_blocked() -> None:
    """Example of improper async/await usage that blocks the event loop.

    This function uses time.sleep() which blocks the entire thread,
    preventing other async tasks from running during the sleep period.
    This defeats the purpose of async/await and should be avoided. Always
    use await asyncio.sleep() instead of time.sleep() in async functions.

    Warning:
        This is an anti-pattern. Do not use blocking operations like
        time.sleep() in async functions. Use asyncio.sleep() instead.

    Returns:
        None. This is a coroutine that must be awaited, but it will block.
    """
    sleep(1)
