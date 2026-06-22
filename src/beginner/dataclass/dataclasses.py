"""Dataclass examples demonstrating Python's dataclass decorator.

This module shows how to use dataclasses for creating classes that primarily
store data, with automatic generation of special methods. Includes examples
of properties, calculated fields, and argument unpacking.
"""

from dataclasses import dataclass
from math import pi


@dataclass
class Circle:
    """Circle Class."""

    radius: float
    decimal_precision: int

    @property
    def diameter(self) -> float:
        """Return the diameter of the circle.

        Returns:
            Diameter of the circle
        """
        diameter = 2 * self.radius
        return round(diameter, self.decimal_precision)

    @property
    def area(self) -> float:
        """Return the area of the circle.

        Returns:
            Area of the circle
        """
        area: float = (self.radius**2) * pi
        return round(area, self.decimal_precision)

    @property
    def perimeter(self) -> float:
        """Return the perimeter of the circle.

        Returns:
            Perimeter of the circle
        """
        perimeter: float = 2 * self.radius * pi
        return round(perimeter, self.decimal_precision)

    @classmethod
    def set_circle_args(cls, *args) -> "Circle":
        """Set a Circle instance with positional arguments.

        Other Parameters:
            r (float): Positional argument to create a Circle class,
                represents the radius
            d (int): Positional argument to create a Circle class,
                represents the decimal precision
        Returns:
            A circle instance
        """
        circle: Circle = cls(*args)
        return circle

    @classmethod
    def set_circle_kwargs(cls, **kwargs) -> "Circle":
        """Set a Circle instance with keyword arguments.

        Other Parameters:
            radius (float): Keyword argument to create a Circle class,
                represents the radius
            decimal_precision (int): Keyword argument to create a Circle class,
                represents the decimal precision
        Returns:
            A circle instance
        """
        circle_kwargs: Circle = cls(**kwargs)
        return circle_kwargs
