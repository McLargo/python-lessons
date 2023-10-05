from collections import defaultdict
from typing import Optional


def get_value_from_key_with_square_brackets(
    my_dict: dict[str, str],
    key: str,
) -> str:
    """
    Get value from a dict using square brackets.

    Parameters:
        my_dict (dict[str, str]): dict to find value.
        key (str): key to find in the dict.

    Returns:
        value (str): value of the dict for the key provided.

    Raises:
        KeyError: If key is not in the dict.
    """
    return my_dict[key]


def get_value_from_key_with_get(
    my_dict: dict[str, str],
    key: str,
    default: str = None,
) -> Optional[str]:
    """
    Get value from a dict using get method.
    Return default if key is not in the dict.

    Parameters:
        my_dict (dict[str, str]): dict to find value.
        key (str): key to find in the dict.
        default (str): default value to return if key is not in the
            dict.

    Returns:
        value (str, None): value of the dict for the key provided.
    """
    return my_dict.get(key, default)


def get_value_from_defaultdict(
    my_dict: dict[str, str],
    key: str,
    default: str = None,
) -> str:
    """
    Get value from a defaultdict using square brackets.

    Parameters:
        my_dict (dict[str, str]): defaultdict to find value.
        key (str): key to find in the defaultdict.
        default (str): default value class to return if key is not in the
            defaultdict.

    Returns:
        value (str): value of the defaultdict for the key provided.
    """
    default_dict = defaultdict(lambda: default)
    default_dict.update(**my_dict)
    return default_dict[key]
