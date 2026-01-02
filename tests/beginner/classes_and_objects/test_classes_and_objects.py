from beginner.classes_and_objects import IngredientEnum, Pizza


def test_pizza() -> None:
    pizza: Pizza = Pizza(
        ingredients=[
            IngredientEnum.TOMATO,
            IngredientEnum.BASIL,
            IngredientEnum.MOZZARELLA,
            IngredientEnum.HAM,
            IngredientEnum.ONION,
        ],
    )
    assert isinstance(pizza, Pizza) is True
    assert len(pizza.ingredients) == 5  # noqa: PLR2004
    assert pizza.price() == 15  # noqa: PLR2004


def test_pizza_napolitana() -> None:
    pizza_napolitana: Pizza = Pizza.napolitana()
    assert isinstance(pizza_napolitana, Pizza) is True
    assert len(pizza_napolitana.ingredients) == 3  # noqa: PLR2004
    assert pizza_napolitana.price() == 9  # noqa: PLR2004


def test_pizza_four_cheese() -> None:
    pizza_four_cheese: Pizza = Pizza.four_cheese()
    assert isinstance(pizza_four_cheese, Pizza) is True
    assert len(pizza_four_cheese.ingredients) == 4  # noqa: PLR2004
    assert pizza_four_cheese.price() == 12  # noqa: PLR2004


def test_change_price_per_ingredient() -> None:
    pizza_napolitana: Pizza = Pizza.napolitana()
    assert pizza_napolitana.price() == 9  # noqa: PLR2004

    pizza_four_cheese: Pizza = Pizza.four_cheese()
    assert pizza_four_cheese.price() == 12  # noqa: PLR2004

    # updating a class attribute, AFFECTS ALL INSTANCES!
    Pizza.price_per_ingredient = 3.5
    assert pizza_napolitana.price() == 10.5  # noqa: PLR2004
    assert pizza_four_cheese.price() == 14.0  # noqa: PLR2004

    # updating class attribute to original value
    Pizza.price_per_ingredient = 3


def test_list_all_ingredients() -> None:
    ingredients: list[IngredientEnum] = Pizza.list_all_ingredients()
    for ingredient in ingredients:
        assert isinstance(ingredient, IngredientEnum) is True
        assert isinstance(ingredient.value, str) is True
