"""Dataclass examples demonstrating Python's dataclass decorator.

This module shows how to use dataclasses for creating classes that primarily
store data, with automatic generation of special methods. Includes examples
of properties, calculated fields, and argument unpacking.
"""

from dataclasses import dataclass
from math import pi
from typing import Any


@dataclass
class Circle:
    """Circle class demonstrating dataclass features with calculated properties.

    This class uses the @dataclass decorator to automatically generate
    __init__, __repr__, and other special methods. It includes properties
    for calculating geometric measurements (diameter, area, perimeter) with
    configurable decimal precision.

    Attributes:
        radius: The radius of the circle in any unit (e.g., meters, inches).
        decimal_precision: Number of decimal places to round calculations to.
    """

    radius: float
    decimal_precision: int

    @property
    def diameter(self) -> float:
        """Calculate and return the diameter of the circle.

        The diameter is twice the radius. The result is rounded to the
        configured decimal precision.

        Returns:
            The diameter of the circle, rounded to decimal_precision places.
        """
        diameter = 2 * self.radius
        return round(diameter, self.decimal_precision)

    @property
    def area(self) -> float:
        """Calculate and return the area of the circle.

        Uses the formula A = πr² where r is the radius. The result is
        rounded to the configured decimal precision.

        Returns:
            The area of the circle, rounded to decimal_precision places.
        """
        area: float = (self.radius**2) * pi
        return round(area, self.decimal_precision)

    @property
    def perimeter(self) -> float:
        """Calculate and return the perimeter of the circle.

        Uses the formula C = 2πr where r is the radius. The result is
        rounded to the configured decimal precision.

        Returns:
            The perimeter of the circle, rounded to decimal_precision places.
        """
        perimeter: float = 2 * self.radius * pi
        return round(perimeter, self.decimal_precision)

    @classmethod
    def set_circle_args(cls, *args: Any) -> "Circle":
        """Create a Circle instance from positional arguments.

        Demonstrates how to use *args to unpack positional arguments
        when creating a dataclass instance. The arguments are passed
        in order: radius, then decimal_precision.

        Args:
            *args: Variable length argument list. Expected arguments:
                - args[0] (float): The radius of the circle
                - args[1] (int): The decimal precision for calculations

        Returns:
            A new Circle instance created with the provided arguments.
        """
        circle: Circle = cls(*args)
        return circle

    @classmethod
    def set_circle_kwargs(cls, **kwargs: Any) -> "Circle":
        """Create a Circle instance from keyword arguments.

        Demonstrates how to use **kwargs to unpack keyword arguments
        when creating a dataclass instance. The arguments must match
        the attribute names defined in the dataclass.

        Args:
            **kwargs: Variable keyword arguments. Expected arguments:
                - radius (float): The radius of the circle
                - decimal_precision (int): The decimal precision for
                  calculations

        Returns:
            A new Circle instance created with the provided keyword
            arguments.
        """
        circle_kwargs: Circle = cls(**kwargs)
        return circle_kwargs
