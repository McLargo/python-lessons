import sys
from typing import Generator

from src.intermediate.yield_vs_return import (
    return_even_numbers,
    yield_even_numbers,
    yield_fibonacci_numbers,
)


def test_return_even_numbers() -> None:
    even_numbers: list[int] = return_even_numbers(10)
    assert isinstance(even_numbers, list)
    assert even_numbers == [2, 4, 6, 8]


def test_yield_even_numbers() -> None:
    even_numbers: Generator = yield_even_numbers(10)
    assert isinstance(even_numbers, Generator)
    assert list(even_numbers) == [2, 4, 6, 8]
    # generator is exhausted
    assert list(even_numbers) == []


def test_memory_difference_yield_vs_return() -> None:
    list_even_numbers: list[int] = return_even_numbers(100)
    assert isinstance(list_even_numbers, list)
    generator_even_numbers: Generator = yield_even_numbers(100)
    assert isinstance(generator_even_numbers, Generator)
    assert sys.getsizeof(list_even_numbers) > sys.getsizeof(
        generator_even_numbers,
    )


def test_yield_fibonacci() -> None:
    fibonacci_numbers: Generator = yield_fibonacci_numbers()
    assert isinstance(fibonacci_numbers, Generator)
    expected_fibonacci_numbers: list[int] = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i in range(10):
        fibonacci_number: int = next(fibonacci_numbers)
        assert isinstance(fibonacci_number, int)
        assert fibonacci_number == expected_fibonacci_numbers[i]
