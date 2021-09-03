from beginner.class_methods import Pizza


def test_pizza_price():
    pizza_napolitana = Pizza.napolitana()
    assert isinstance(pizza_napolitana, Pizza) is True
    assert pizza_napolitana.price == 9
    pizza_four_cheese = Pizza.four_cheese()
    assert isinstance(pizza_four_cheese, Pizza) is True
    assert pizza_four_cheese.price == 12
    # lets imagine that four cheese pizza needs to update price_per_ingredient to 4
    # If you change Pizza.price_per_ingredient it will affect to all Pizza instances
    Pizza.price_per_ingredient = 4
    assert pizza_napolitana.price != 9
    assert pizza_four_cheese.price == 16
    # for that, we need to update that value in the corresponding instance only
    Pizza.price_per_ingredient = 3
    assert pizza_napolitana.price == 9
    pizza_four_cheese.price_per_ingredient = 4
    assert pizza_four_cheese.price == 16
