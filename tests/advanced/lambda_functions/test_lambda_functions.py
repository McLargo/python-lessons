import pytest
from advanced.lambda_functions.lambda_functions import (
    filter_by_applying_function_to_elements,
    get_list_of_fields_from_a_list_dict,
    sort_a_list_of_dict_by_a_field,
)
from hypothesis import given
from hypothesis import strategies as st

cars = [
    {"brand": "Toyota", "model": "Avensis", "release_year": 2003},
    {"brand": "Saab", "model": "900 Turbo", "release_year": 1978},
    {"brand": "Volkswagen", "model": "Golf GTI", "release_year": 1976},
]

numbers = [1, 5, 8, 20, 3, 11, 78]


def test_get_a_field_from_a_list_of_dict() -> None:
    brands = get_list_of_fields_from_a_list_dict(cars, "brand")
    expected_brands = ["Toyota", "Saab", "Volkswagen"]

    assert all([a == b for a, b in zip(brands, expected_brands)])


def test_get_list_dict_sorted_by_a_field() -> None:
    expected_brands_sorted_by_model_asc = ["Saab", "Toyota", "Volkswagen"]

    cars_sorted_by_model_asc = sort_a_list_of_dict_by_a_field(cars, "model")
    brands_sorted_asc = get_list_of_fields_from_a_list_dict(
        cars_sorted_by_model_asc,
        "brand",
    )
    assert all(
        [
            a == b
            for a, b in zip(
                brands_sorted_asc,
                expected_brands_sorted_by_model_asc,
            )
        ],
    )

    expected_brands_sorted_by_release_year_dsc = [
        "Toyota",
        "Saab",
        "Volkswagen",
    ]
    cars_sorted_by_release_year_dsc = sort_a_list_of_dict_by_a_field(
        cars,
        "release_year",
        False,
    )
    brands_sorted_dsc = get_list_of_fields_from_a_list_dict(
        cars_sorted_by_release_year_dsc,
        "brand",
    )
    assert all(
        [
            a == b
            for a, b in zip(
                brands_sorted_dsc,
                expected_brands_sorted_by_release_year_dsc,
            )
        ],
    )


def test_pass_an_even_lambda_function_as_argument() -> None:
    expected_even_numbers = [8, 20, 78]
    even_numbers = filter_by_applying_function_to_elements(
        lambda x: x % 2 == 0,
        numbers,
    )
    assert all([a == b for a, b in zip(even_numbers, expected_even_numbers)])


def test_pass_an_odd_lambda_function_as_argument() -> None:
    expected_odd_numbers = [1, 5, 3, 11]
    odd_numbers = filter_by_applying_function_to_elements(
        lambda x: x % 2 != 0,
        numbers,
    )
    assert all([a == b for a, b in zip(odd_numbers, expected_odd_numbers)])


def test_pass_a_startswith_lambda_function_as_argument() -> None:
    strings = ["a", "aa", "ba", "cc", "ax"]
    expected_start_with_a = ["a", "aa", "ax"]
    start_with_a = filter_by_applying_function_to_elements(
        lambda x: x.startswith("a"),
        strings,
    )
    assert all([a == b for a, b in zip(start_with_a, expected_start_with_a)])


@pytest.mark.parametrize(
    ("field", "expected"),
    [
        ("brand", ["Toyota", "Saab", "Volkswagen"]),
        ("model", ["Avensis", "900 Turbo", "Golf GTI"]),
        ("release_year", [2003, 1978, 1976]),
    ],
)
def test_extract_any_field_from_list_of_dicts(field, expected):
    # The `map(lambda d: d[field], ...)` idiom works uniformly for any
    # field name and any value type (str, int, ...).
    assert get_list_of_fields_from_a_list_dict(cars, field) == expected


@pytest.mark.parametrize(
    ("field", "asc", "expected_brands_in_order"),
    [
        ("release_year", True, ["Volkswagen", "Saab", "Toyota"]),
        ("release_year", False, ["Toyota", "Saab", "Volkswagen"]),
        ("brand", True, ["Saab", "Toyota", "Volkswagen"]),
        ("brand", False, ["Volkswagen", "Toyota", "Saab"]),
    ],
)
def test_sort_by_any_field_asc_or_desc(field, asc, expected_brands_in_order):
    # `sorted(..., key=lambda d: d[field], reverse=not asc)` reads as a
    # concrete worked example of the doc's "sorting by a field" section.
    sorted_cars = sort_a_list_of_dict_by_a_field(cars, field, asc=asc)

    assert [c["brand"] for c in sorted_cars] == expected_brands_in_order


@pytest.mark.parametrize(
    ("predicate", "elements", "expected"),
    [
        (lambda x: x > 10, [1, 5, 8, 20, 3, 11, 78], [20, 11, 78]),
        (lambda x: x < 0, [1, 5, 8], []),
        (
            lambda s: len(s) == 2,
            ["a", "aa", "ba", "cc", "ax"],
            ["aa", "ba", "cc", "ax"],
        ),
        (lambda _: True, [1, 2, 3], [1, 2, 3]),
        (lambda _: False, [1, 2, 3], []),
    ],
)
def test_filter_with_various_lambda_predicates(predicate, elements, expected):
    # Passing a lambda as a first-class value is the whole point of the
    # helper; these cases cover numeric, string, always-true and
    # always-false predicates.
    assert (
        filter_by_applying_function_to_elements(predicate, elements) == expected
    )


def test_late_binding_pitfall_lambda_in_loop_captures_by_reference():
    # Pitfall from the doc: building lambdas in a loop without capturing
    # the loop variable makes every lambda return the LAST value of `i`,
    # because closures capture by reference, not by value.
    functions = []
    for i in range(5):
        functions.append(lambda: i)

    # All five lambdas return the final value of `i` (4), not 0..4.
    assert [f() for f in functions] == [4, 4, 4, 4, 4]


def test_late_binding_fix_default_argument_captures_by_value():
    # Doc-recommended fix: bind the current value of `i` as a default
    # argument, which is evaluated at lambda-definition time.
    functions = []
    for i in range(5):
        functions.append(lambda i=i: i)

    assert [f() for f in functions] == [0, 1, 2, 3, 4]


def test_closure_reflects_later_reassignment_of_captured_variable():
    # Related gotcha: a lambda that captures an outer variable reads its
    # CURRENT value each time it is called, so reassigning the variable
    # after defining the lambda changes the lambda's output.
    multiplier = 2
    multiply = lambda x: x * multiplier  # noqa: E731

    assert multiply(10) == 20

    multiplier = 5

    assert multiply(10) == 50


def test_factory_captures_argument_by_value_via_new_scope():
    # Doc-recommended alternative: wrap the lambda in a factory function
    # so each returned lambda closes over its own parameter binding.
    def create_multiplier(multiplier):
        return lambda x: x * multiplier

    times_two = create_multiplier(2)
    times_five = create_multiplier(5)

    assert times_two(10) == 20
    assert times_five(10) == 50


@given(st.lists(st.integers()))
def test_filter_with_true_lambda_returns_all_elements(elements):
    # Filtering with an always-true predicate must return the input
    # unchanged; a foundational property of `filter`.
    assert (
        filter_by_applying_function_to_elements(lambda _: True, elements)
        == elements
    )


@given(st.lists(st.integers()))
def test_filter_with_false_lambda_returns_empty_list(elements):
    # Filtering with an always-false predicate must return an empty list.
    assert (
        filter_by_applying_function_to_elements(lambda _: False, elements) == []
    )


@given(st.lists(st.integers(), min_size=1))
def test_sort_ascending_is_reverse_of_descending(values):
    # Sorting the same data ascending vs descending must produce lists
    # that are the exact reverse of each other.
    data = [{"n": v} for v in values]

    asc = sort_a_list_of_dict_by_a_field(data, "n", asc=True)
    desc = sort_a_list_of_dict_by_a_field(data, "n", asc=False)

    assert asc == list(reversed(desc))
