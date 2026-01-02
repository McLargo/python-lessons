import pytest

from beginner.dataclasses import Circle


def test_circle_with_args():
    radius = 3
    decimal_precision = 3
    circle: Circle = Circle.set_circle_args(radius, decimal_precision)

    assert isinstance(circle, Circle) is True
    assert circle.radius == 3
    assert circle.area == 28.274
    assert circle.perimeter == 18.85
    assert circle.diameter == 6


def test_circle_with_args_no_args():
    with pytest.raises(TypeError):
        Circle.set_circle_args()

    radius = 3
    decimal_precision = 3
    with pytest.raises(TypeError):
        Circle.set_circle_args(
            radius=radius,
            decimal_precision=decimal_precision,
        )


def test_circle_with_kwargs():
    radius = 3
    decimal_precision = 2
    circle: Circle = Circle.set_circle_kwargs(
        radius=radius,
        decimal_precision=decimal_precision,
    )
    assert isinstance(circle, Circle) is True
    assert circle.radius == 3
    assert circle.area == 28.27
    assert circle.perimeter == 18.85
    assert circle.diameter == 6


def test_circle_with_kwargs_no_kwargs():
    with pytest.raises(TypeError):
        Circle.set_circle_kwargs()

    radius = 3
    decimal_precision = 3
    with pytest.raises(TypeError):
        Circle.set_circle_kwargs(radius, decimal_precision)
