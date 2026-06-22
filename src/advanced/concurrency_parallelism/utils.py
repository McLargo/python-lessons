"""Utility functions and constants for concurrency and parallelism examples.

This module provides helper functions for checking prime numbers and
constants used across concurrency and parallelism demonstrations. These
utilities are intentionally compute-intensive to showcase the benefits
of parallel and concurrent execution.

Constants:
    WORKERS: Number of worker processes/threads to use in pool executors.
    PRIMES: List of large numbers used for prime checking benchmarks.
"""

import math
import os

WORKERS = 4
PRIMES = [
    999999999999988,
    999999999999989,
    999999999999990,
    1000000000000091,
    1000000000000092,
    1000000000000159,
    1000000000000160,
]


def is_prime(n: int) -> bool:
    """Check if a number is prime using trial division.

    This implementation uses trial division which is not the most efficient
    algorithm for large numbers, but it's sufficient for demonstrating
    concurrency and parallelism patterns. The computational intensity makes
    it ideal for benchmarking parallel execution.

    Args:
        n: The number to check. Should be a positive integer.

    Returns:
        True if n is prime, False otherwise.

    Examples:
        >>> is_prime(7)
        True
        >>> is_prime(10)
        False
    """
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def is_prime_with_pid(n: int) -> tuple[int, bool, int]:
    """Check if a number is prime and return the process ID.

    This function wraps is_prime() and additionally captures the process ID
    to demonstrate that different processes handle different numbers in
    parallel execution. The process ID allows us to verify that work is
    actually distributed across multiple processes.

    Args:
        n: The number to check. Should be a positive integer.

    Returns:
        A tuple containing (number, is_prime_result, process_id) where:
            - number: The input number n
            - is_prime_result: Boolean indicating if n is prime
            - process_id: The OS process ID that performed the calculation

    Examples:
        >>> result = is_prime_with_pid(7)
        >>> result[0], result[1], result[2]
        (7, True, <process_id>)
    """
    return (n, is_prime(n), os.getpid())
