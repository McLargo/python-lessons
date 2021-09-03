"""
Sample of staticmethod decorator.

All method inside class Calculator are static method,
which means there is no internal dependency with any attribute or method
of the same class, and can be used without initialize Calculator class
"""


class Calculator:
    @staticmethod
    def add_numbers(x, y):
        """Sum two numbers

        :param int, float x: first integer to sum
        :param int, float y: second integer to sum
        :raises TypeError: params are not int or float
        :returns: sum of 2 params
        :rtype: int, float
        """
        return x + y

    @staticmethod
    def subtract_numbers(x, y):
        """Substract two numbers

        :param int, float x: first integer to substract
        :param int, float y: second integer to substract
        :raises TypeError: params are not int or float
        :returns: difference bewteen first and second params
        :rtype: int, float
        """
        return x - y

    @staticmethod
    def multiple_numbers(x, y):
        """Multiple two numbers

        :param int, float x: first integer to multiple
        :param int, float y: second integer to multiple
        :raises TypeError: params are not int or float
        :returns: multiplication of 2 params
        :rtype: int, float
        """
        return x * y

    @staticmethod
    def divide_numbers(x, y):
        """Divide two numbers

        :param int, float x: first integer to divide
        :param int, float y: second integer to divide
        :raises TypeError: params are not int or float
        :returns: quotient of first and second param
        :rtype: int, float
        """
        return x // y
