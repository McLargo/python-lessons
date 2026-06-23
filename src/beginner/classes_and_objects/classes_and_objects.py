"""Module to set an instance of a Pizza with Ingredients.

This module contains the enum for all ingredients available to create a Pizza,
and the class to create a Pizza instance.

"""

from enum import Enum


class IngredientEnum(Enum):
    """Enumeration of all available pizza ingredients.

    This enum defines the complete set of ingredients that can be used
    to customize a pizza. Using an enum ensures type safety and provides
    a clear inventory of available options.
    """

    MOZZARELLA = "mozzarella"
    TOMATO = "tomato"
    BASIL = "basil"
    GORGONZOLA = "gorgonzola"
    EMMENTAL = "emmental"
    PARMESAN = "parmesan"
    HAM = "ham"
    TUNA = "tuna"
    ONION = "onion"


class Pizza:
    """Represents a pizza with customizable ingredients and pricing.

    This class demonstrates key object-oriented concepts including:
    - Class attributes (shared across all instances)
    - Instance attributes (unique to each instance)
    - Class methods for creating predefined pizza types
    - Static methods for utility functions
    - Instance methods for calculations

    Attributes:
        price_per_ingredient: Base price for each ingredient. This is a
            class attribute shared by all Pizza instances. Defaults to 3.
        ingredients: List of ingredients in this specific pizza. This is an
            instance attribute unique to each Pizza.
    """

    price_per_ingredient: float = 3

    def __init__(self, ingredients: list[IngredientEnum]) -> None:
        """Initialize a Pizza with a list of ingredients.

        Args:
            ingredients: List of ingredients to include in the pizza.
                Each ingredient must be from the IngredientEnum.
        """
        self.ingredients: list[IngredientEnum] = ingredients

    @classmethod
    def napolitana(cls) -> "Pizza":
        """Create a Napolitana (Margherita) pizza with traditional ingredients.

        This class method demonstrates the factory pattern for creating
        specific pizza types. All Napolitana pizzas have the same standard
        ingredients: basil, tomato, and mozzarella.

        Returns:
            A new Pizza instance with Napolitana ingredients.
        """
        ingredients = [
            IngredientEnum.BASIL,
            IngredientEnum.TOMATO,
            IngredientEnum.MOZZARELLA,
        ]
        return cls(ingredients=ingredients)

    @classmethod
    def four_cheese(cls) -> "Pizza":
        """Create a Four Cheese pizza.

        This class method demonstrates the factory pattern for creating
        specific pizza types. All Four Cheese pizzas have the same standard
        ingredients: gorgonzola, mozzarella, emmental, and parmesan.

        Returns:
            A new Pizza instance with Four Cheese ingredients.
        """
        ingredients = [
            IngredientEnum.GORGONZOLA,
            IngredientEnum.MOZZARELLA,
            IngredientEnum.EMMENTAL,
            IngredientEnum.PARMESAN,
        ]
        return cls(ingredients=ingredients)

    def price(self) -> float:
        """Calculate the total price of this pizza.

        The price is calculated by multiplying the number of ingredients
        by the price_per_ingredient class attribute. This demonstrates
        how instance methods can access both instance and class attributes.

        Returns:
            The total price for this pizza based on its ingredients.
        """
        return len(self.ingredients) * self.price_per_ingredient

    @staticmethod
    def list_all_ingredients() -> list[IngredientEnum]:
        """List all available ingredients for creating pizzas.

        This static method demonstrates a utility function that doesn't
        need access to instance or class attributes. It provides a convenient
        way to retrieve all possible ingredients from the IngredientEnum.

        Returns:
            A list of all IngredientEnum values representing available
            ingredients.
        """
        return [ingredient for ingredient in IngredientEnum]
