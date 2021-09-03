"""
Sample of classmethod decorator.

A classmethod is a method that is associated to the class, and not an object.
We can use it to easily create objects of the class.

Careful, updating a class state will affect to all instance!
"""


class Pizza:

    ingredients = []
    price_per_ingredient = 3

    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def napolitana(cls):
        """Create a Pizza instance with mozzarella, tomato and basil

        :param cls: Pizza class
        :returns: Pizza instance
        :rtype: Pizza
        """
        ingredients = ["mozzarella", "tomato", "basil"]
        return cls(ingredients=ingredients)

    @classmethod
    def four_cheese(cls):
        """Create a Pizza instance with blue cheese, mozzarella,
        emmental and parmesan

        :param cls: Pizza class
        :returns: Pizza instance
        :rtype: Pizza
        """
        ingredients = ["blue cheese", "mozzarella", "emmental", "parmesan"]
        return cls(ingredients=ingredients)

    @property
    def price(self):
        """price of a Pizza. total ingredients * price_per_ingredient

        :returns: pizza price per ingredient
        :rtype: int, Float
        """
        return len(self.ingredients) * self.price_per_ingredient
