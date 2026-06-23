"""Parallel examples using ProcessPoolExecutor and multiprocessing Pool."""

from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Pool

from advanced.concurrency_parallelism.utils import (
    PRIMES,
    WORKERS,
    is_prime_with_pid,
)


def parallelism_with_multiprocess() -> list[tuple[int, bool, int]]:
    """Example of multiprocessing to check if a number is prime.

    Uses Python's multiprocessing Pool to distribute prime checking
    across multiple processes. Each process runs independently with
    its own memory space, avoiding the GIL limitation.

    Returns:
        List of tuples where each tuple contains
        (number, is_prime_result, process_id).
        The process_id varies across tuples as different processes
        handle different numbers.
    """
    with Pool(WORKERS) as p:
        return p.map(is_prime_with_pid, PRIMES)


def parallelism_with_concurrent_process_pool() -> list[tuple[int, bool, int]]:
    """Example of ProcessPoolExecutor to check if a number is prime.

    Uses concurrent.futures.ProcessPoolExecutor for process-based parallelism.
    This provides a higher-level interface than multiprocessing.Pool with
    better integration with Python's concurrent.futures API.

    Returns:
        List of tuples where each tuple contains
        (number, is_prime_result, process_id).
        The process_id varies as the executor distributes work across
        the worker pool.
    """
    with ProcessPoolExecutor(WORKERS) as executor:
        return list(executor.map(is_prime_with_pid, PRIMES))
