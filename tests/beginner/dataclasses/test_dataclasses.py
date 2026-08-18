import math

import pytest
from beginner.dataclass import Circle
from hypothesis import given
from hypothesis import strategies as st


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


def test_dataclass_auto_generated_init_accepts_positional_and_keyword():
    # The @dataclass decorator auto-generates __init__ from the annotated
    # fields, so both positional and keyword construction are supported
    # out of the box, without writing any __init__ ourselves.
    positional = Circle(2, 2)
    keyword = Circle(radius=2, decimal_precision=2)

    assert positional.radius == 2
    assert positional.decimal_precision == 2
    assert keyword.radius == 2
    assert keyword.decimal_precision == 2


def test_dataclass_auto_generated_repr_shows_field_values():
    # @dataclass auto-generates a readable __repr__ containing every field,
    # which is one of the main productivity benefits over a plain class.
    circle = Circle(radius=5, decimal_precision=2)

    assert repr(circle) == "Circle(radius=5, decimal_precision=2)"


def test_dataclass_auto_generated_eq_compares_by_field_values():
    # @dataclass auto-generates __eq__ so two instances with the same field
    # values compare equal, unlike a plain class whose default __eq__ is
    # identity-based.
    a = Circle(radius=3, decimal_precision=2)
    b = Circle(radius=3, decimal_precision=2)
    c = Circle(radius=3, decimal_precision=3)

    assert a == b
    assert a is not b
    assert a != c


@pytest.mark.parametrize(
    (
        "radius",
        "precision",
        "expected_diameter",
        "expected_perimeter",
        "expected_area",
    ),
    [
        (1, 4, 2, 6.2832, 3.1416),
        (2, 3, 4, 12.566, 12.566),
        (5, 2, 10, 31.42, 78.54),
        (10, 1, 20, 62.8, 314.2),
        (0, 2, 0, 0.0, 0.0),
    ],
)
def test_properties_compute_expected_geometry(
    radius,
    precision,
    expected_diameter,
    expected_perimeter,
    expected_area,
):
    # Properties are computed on access (not stored), and each property
    # honours the configured decimal_precision.
    circle = Circle(radius=radius, decimal_precision=precision)

    assert circle.diameter == expected_diameter
    assert circle.perimeter == expected_perimeter
    assert circle.area == expected_area


@pytest.mark.parametrize("precision", [0, 1, 2, 3, 4, 5])
def test_decimal_precision_controls_rounding(precision):
    # The same radius produces different rounded outputs for different
    # decimal_precision values, showing the field is used at read time.
    circle = Circle(radius=1, decimal_precision=precision)

    assert circle.area == round(math.pi, precision)
    assert circle.perimeter == round(2 * math.pi, precision)


@given(radius=st.floats(min_value=0.1, max_value=1_000.0, allow_nan=False))
def test_property_diameter_is_twice_the_radius(radius):
    # Property invariant: diameter is exactly 2 * radius (rounded).
    circle = Circle(radius=radius, decimal_precision=6)

    assert circle.diameter == round(2 * radius, 6)


@given(radius=st.floats(min_value=0.1, max_value=1_000.0, allow_nan=False))
def test_property_area_follows_pi_r_squared(radius):
    # Property invariant: area equals pi * r**2 (rounded).
    circle = Circle(radius=radius, decimal_precision=6)

    assert circle.area == round(math.pi * radius**2, 6)
