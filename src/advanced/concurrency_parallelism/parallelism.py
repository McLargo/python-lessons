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

    Returns:
        list: List of tuples (number, is_prime_result, process_id)
    """
    with Pool(WORKERS) as p:
        return p.map(is_prime_with_pid, PRIMES)


def parallelism_with_concurrent_process_pool() -> list[tuple[int, bool, int]]:
    """Example of ProcessPoolExecutor to check if a number is prime."""
    with ProcessPoolExecutor(WORKERS) as executor:
        return list(executor.map(is_prime_with_pid, PRIMES))
