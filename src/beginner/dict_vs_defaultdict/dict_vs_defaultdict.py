"""Module to compare dict vs defaultdict.

This module contains the functions to compare the use and performance of dict vs
defaultdict.

"""

from collections import defaultdict


def get_value_from_dict_with_square_brackets(
    my_dict: dict[str, str],
    key: str,
) -> str:
    """Get value from a dict using square brackets.

    This demonstrates direct dictionary access using square bracket notation.
    This approach raises a KeyError if the key doesn't exist, which can be
    useful when you want to ensure the key is present.

    Args:
        my_dict: Dictionary with string keys and string values
            to search for the value.
        key: Key to look up in the dictionary.

    Returns:
        The value associated with the key in the dictionary.

    Raises:
        KeyError: If the key is not found in the dictionary.
    """
    return my_dict[key]


def get_value_from_dict_with_get(
    my_dict: dict[str, str],
    key: str,
    default: str | None = None,
) -> str | None:
    """Get value from a dict using get method.

    The get() method provides a safe way to access dictionary values,
    returning a default value instead of raising KeyError when the key
    is not found. This is preferred when missing keys are expected.

    Args:
        my_dict: Dictionary with string keys and string values
            to search for the value.
        key: Key to look up in the dictionary.
        default: Value to return if key is not found. Defaults to None.

    Returns:
        The value associated with the key, or the default value if the
        key is not found.
    """
    return my_dict.get(key, default)


def get_value_from_defaultdict(
    my_dict: dict[str, str],
    key: str,
    default: str | None = None,
) -> str | None:
    """Get value from a defaultdict using square brackets.

    Demonstrates how defaultdict automatically provides default values for
    missing keys. When a lambda function is passed to defaultdict, it's
    called to generate the default value whenever a missing key is accessed.

    Args:
        my_dict: Regular dictionary with string keys and string values
            to convert to defaultdict.
        key: Key to look up in the defaultdict.
        default: Value that the lambda function should return for missing
            keys. Defaults to None.

    Returns:
        The value associated with the key, or the default value if the
        key was not in the original dictionary.
    """
    default_dict: defaultdict[str, str | None] = defaultdict(lambda: default)
    default_dict.update(**my_dict)
    return default_dict[key]
