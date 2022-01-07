"""

"""


class ExtendedCalculator:
    @staticmethod
    def add_several_numbers(*args):
        """Sum two numbers

        :param int, float x: first integer to sum
        :param int, float y: second integer to sum
        :raises TypeError: params are not int or float
        :returns: sum of 2 params
        :rtype: int, float
        """
        total = 0
        for number in args:
            total += number
        return total

    @staticmethod
    def add_even_numbers(*args):
        """Sum two numbers

        :param int, float x: first integer to sum
        :param int, float y: second integer to sum
        :raises TypeError: params are not int or float
        :returns: sum of 2 params
        :rtype: int, float
        """
        total_even = 0
        for number in args:
            if number % 2 == 0:
                total_even += number
        return total_even

    @staticmethod
    def add_prime_numbers(**kwargs):
        """Sum two numbers

        :param int, float x: first integer to sum
        :param int, float y: second integer to sum
        :raises TypeError: params are not int or float
        :returns: sum of 2 params
        :rtype: int, float
        """
        total_prime = 0
        for key, number in kwargs.items():
            if key == "prime":
                total_prime += number
        return total_prime


def test_add_several_numbers():
    assert ExtendedCalculator.add_several_numbers(1, 2, 3) == 6
    assert ExtendedCalculator.add_several_numbers(xrange(10)) == 6


def test_add_even_numbers():
    assert ExtendedCalculator.add_even_numbers(1, 2, 3) == 2
    assert ExtendedCalculator.add_even_numbers(xrange(10)) == 6


def test_big_n():
    numbers = {"small": 12}
    assert ExtendedCalculator.add_several_numbers(1, 2, 3) == 6
    assert ExtendedCalculator.add_several_numbers(xrange(10)) == 6
