from src.advanced.lambda_functions.lambda_functions import (
    filter_by_applying_function_to_elements,
    get_list_of_fields_from_a_list_dict,
    sort_a_list_of_dict_by_a_field,
)

cars = [
    {"brand": "Toyota", "model": "Avensis", "release_year": 2003},
    {"brand": "Saab", "model": "900 Turbo", "release_year": 1978},
    {"brand": "Volkswagen", "model": "Golf GTI", "release_year": 1976},
]


def test_get_a_field_from_a_list_of_dict() -> None:
    brands = get_list_of_fields_from_a_list_dict(cars, "brand")
    expected_brands = ["Toyota", "Saab", "Volkswagen"]

    assert all([a == b for a, b in zip(brands, expected_brands)])


def test_get_list_dict_sorted_by_a_field() -> None:
    cars = [
        {"brand": "Toyota", "model": "Avensis", "release_year": 2003},
        {"brand": "Saab", "model": "900 Turbo", "release_year": 1978},
        {"brand": "Volkswagen", "model": "Golf GTI", "release_year": 1976},
    ]

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


def test_pass_a_lambda_function_as_argument() -> None:
    numbers = [1, 5, 8, 20, 3, 11, 78]

    expected_even_numbers = [8, 20, 78]
    even_numbers = filter_by_applying_function_to_elements(
        lambda x: x % 2 == 0,
        numbers,
    )
    assert all([a == b for a, b in zip(even_numbers, expected_even_numbers)])

    expected_odd_numbers = [1, 5, 3, 11]
    odd_numbers = filter_by_applying_function_to_elements(
        lambda x: x % 2 != 0,
        numbers,
    )
    assert all([a == b for a, b in zip(odd_numbers, expected_odd_numbers)])

    strings = ["a", "aa", "ba", "cc", "ax"]
    expected_start_with_a = ["a", "aa", "ax"]
    start_with_a = filter_by_applying_function_to_elements(
        lambda x: x.startswith("a"),
        strings,
    )
    assert all([a == b for a, b in zip(start_with_a, expected_start_with_a)])
