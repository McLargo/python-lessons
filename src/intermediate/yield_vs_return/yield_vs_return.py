"""Module to compare yield vs return.

This module contains the functions to compare the use of yield vs return.

"""

from typing import Generator


def return_even_numbers(n: int) -> list[int]:
    """Return a list of all even numbers from 2 up to n (exclusive).

    This function demonstrates the use of return to produce a complete list
    at once. All even numbers are collected in memory before returning,
    which can be memory-intensive for large values of n.

    Args:
        n: The upper limit (exclusive) for generating even numbers.
            Only even numbers less than n will be included.

    Returns:
        A list containing all even numbers from 2 up to (but not including) n.
        Returns an empty list if n <= 2.
    """
    numbers: list[int] = []
    for number in range(2, n):
        if number % 2 == 0:
            numbers.append(number)
    return numbers


def yield_even_numbers(n: int) -> Generator:
    """Yield even numbers from 2 up to n (exclusive) one at a time.

    This function demonstrates the use of yield to create a generator.
    Numbers are produced on-demand rather than all at once, making this
    memory-efficient for large values of n. Each number is computed only
    when requested by the caller.

    Args:
        n: The upper limit (exclusive) for generating even numbers.
            Only even numbers less than n will be yielded.

    Yields:
        Even numbers from 2 up to (but not including) n, one at a time.

    Returns:
        A Generator that yields even numbers. The generator is lazy and
        produces values on-demand.
    """
    for number in range(2, n):
        if number % 2 == 0:
            yield number


def yield_fibonacci_numbers() -> Generator:
    """Yield Fibonacci numbers in an infinite sequence.

    This function demonstrates an infinite generator using yield. It produces
    Fibonacci numbers indefinitely without storing them in memory. The caller
    controls how many numbers to consume, making this pattern ideal for
    potentially infinite sequences.

    The Fibonacci sequence starts with 0 and 1, and each subsequent number
    is the sum of the two preceding numbers: 0, 1, 1, 2, 3, 5, 8, 13, ...

    Yields:
        The next number in the Fibonacci sequence, starting from 0.

    Returns:
        A Generator that yields Fibonacci numbers indefinitely. The generator
        will continue producing values until explicitly stopped by the caller.
    """
    c1, c2 = 0, 1
    count = 0
    while True:
        yield c1
        c3 = c1 + c2
        c1 = c2
        c2 = c3
        count += 1
