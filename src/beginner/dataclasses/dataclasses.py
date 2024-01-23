"""Module to set an instance of a Pizza with Ingredients.

This module contains the enum for all ingredients available to create a Pizza,
and the class to create a Pizza instance.

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
