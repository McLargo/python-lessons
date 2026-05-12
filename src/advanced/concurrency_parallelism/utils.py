"""Utils functions for concurrency and parallelism examples."""

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
    """Check if a number is prime.

    Note: this is not the most efficient way to check if a number is prime,
    but it is sufficient for our purposes.
    """
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def is_prime_with_pid(n: int) -> tuple[int, bool, int]:
    """Check if a number is prime and return the process ID.

    Returns:
        tuple: (number, is_prime_result, process_id)
    """
    return (n, is_prime(n), os.getpid())
