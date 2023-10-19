from enum import Enum


class IngredientEnum(Enum):
    """Enum for all ingredients available to customize a Pizza"""

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
    """Class to represent a Pizza.

    Attributes:
        price_per_ingredient (float): price per ingredient. Defaults to 3.
    """

    price_per_ingredient: float = 3

    def __init__(self, ingredients: list[IngredientEnum]) -> None:
        """Constructor for Pizza class
        Args:
            ingredients (list[IngredientEnum]): List of ingredients for a Pizza
        """
        self.ingredients: list[IngredientEnum] = ingredients

    @classmethod
    def napolitana(cls) -> "Pizza":
        """Class Method to create a Napolitana Pizza instance.
        We can create a classmethod, as all napolitana pizzas
        will have the same ingredients.

        Returns:
            Pizza: a Pizza instance.
        """
        ingredients = [
            IngredientEnum.BASIL,
            IngredientEnum.TOMATO,
            IngredientEnum.MOZZARELLA,
        ]
        return cls(ingredients=ingredients)

    @classmethod
    def four_cheese(cls) -> "Pizza":
        """Class Method to create a Four cheese Pizza instance.
        We can create a classmethod, as all four cheese pizzas
        will have the same ingredients.

        Returns:
            Pizza: a Pizza instance.
        """
        ingredients = [
            IngredientEnum.GORGONZOLA,
            IngredientEnum.MOZZARELLA,
            IngredientEnum.EMMENTAL,
            IngredientEnum.PARMESAN,
        ]
        return cls(ingredients=ingredients)

    def price(self) -> float:
        """Method to get price for Pizza instance.
        It depends on the number of ingredients a Pizza has,
        and the price per ingredient.

        Returns:
            float: total price for a Pizza instance.
        """
        return len(self.ingredients) * self.price_per_ingredient

    @staticmethod
    def list_all_ingredients() -> list[IngredientEnum]:
        """Static method to list all ingredients available to create a Pizza.
        It can be a static method, as there is no relation with Pizza instance.

        Returns:
            list[IngredientEnum]: list of ingredients to create a Pizza.
        """
        return [ingredient for ingredient in IngredientEnum]
