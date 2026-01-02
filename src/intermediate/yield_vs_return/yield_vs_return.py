"""Module to compare yield vs return.

This module contains the functions to compare the use of yield vs return.

"""

from typing import Generator


def return_even_numbers(n: int) -> list[int]:
    """Return even numbers until n (inclusive).

    Returns:
        even_numbers: List of even numbers until n (inclusive).
    """
    numbers: list[int] = []
    for number in range(2, n):
        if number % 2 == 0:
            numbers.append(number)
    return numbers


def yield_even_numbers(n: int) -> Generator:
    """Yield even numbers until n (inclusive).

    Returns:
        even_numbers: List of even numbers until n (inclusive).
    """
    for number in range(2, n):
        if number % 2 == 0:
            yield number


def yield_fibonacci_numbers() -> Generator:
    """Yield Fibonacci series.

    Returns:
        fibonacci_numbers: List of numbers of the Fibonacci series.
    """
    c1, c2 = 0, 1
    count = 0
    while True:
        yield c1
        c3 = c1 + c2
        c1 = c2
        c2 = c3
        count += 1
