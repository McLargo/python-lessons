from beginner.static_methods import Calculator
from beginner.use_args_kwargs import ExtendedCalculator


def test_add_numbers():
    assert Calculator.add_numbers(2, 2) == 4
    assert Calculator.add_numbers(2.2, 2.8) == 5.0


def test_subtract_numbers():
    assert Calculator.subtract_numbers(15, 3) == 12
    assert Calculator.subtract_numbers(15.89, 2.7) == 13.190000000000001


def test_multiple_numbers():
    assert Calculator.multiple_numbers(5, 5) == 25
    assert Calculator.multiple_numbers(5.5, 5.5) == 30.25


def test_divide_numbers():
    assert Calculator.divide_numbers(15, 3) == 5
    assert Calculator.divide_numbers(15.9, 3.3) == 4.0
