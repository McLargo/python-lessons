"""Module about lambda functions.

This module contains examples about lambda functions.

"""


from typing import Any, Callable


def get_list_of_fields_from_a_list_dict(
    content: list[dict[str, str]],
    field_to_be_extracted: str,
) -> list[str]:
    """Extract and return a given field from a list of dictionaries.

    Parameters:
        content: list of dictionaries.
        field_to_be_extracted: field to be extracted.

    Returns:
        list[str]: list of the values extracted.
    """
    return map(lambda d: d[field_to_be_extracted], content)


def sort_a_list_of_dict_by_a_field(
    content_to_be_sorted: list[dict],
    sorted_by: str,
    asc: bool = True,
) -> list[dict[str, str]]:
    """Sort a list of dict by a given field.

    Parameters:
        content_to_be_sorted: list of dict to be sorted.
        sorted_by: field to be used for sorting.
        asc: if false, it is sort in descending order. By default, it is true,
            ascending order.

    Returns:
        list[dict]: content sorted.
    """
    return sorted(
        content_to_be_sorted,
        key=lambda d: d[sorted_by],
        reverse=not asc,
    )


def filter_by_applying_function_to_elements(
    func: Callable,
    elements: list[Any],
) -> list[Any]:
    """Apply a function to a list of elements.

    Parameters:
        func: function to apply.
        elements: elements to apply the function.

    Returns:
        list[Any]: the result of apply a function to a list of elements.
    """
    return list(filter(func, elements))
