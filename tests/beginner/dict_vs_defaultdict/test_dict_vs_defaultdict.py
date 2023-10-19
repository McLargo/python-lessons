import pytest

from src.beginner.dict_vs_defaultdict import (
    get_value_from_defaultdict,
    get_value_from_dict_with_get,
    get_value_from_dict_with_square_brackets,
)


def test_get_value_from_dict_with_square_brackets():
    my_dict = {"key": "value"}
    assert get_value_from_dict_with_square_brackets(my_dict, "key") == "value"
    with pytest.raises(KeyError):
        get_value_from_dict_with_square_brackets(my_dict, "key2")


def test_get_value_from_dict_with_get():
    my_dict = {"key": "value"}
    assert get_value_from_dict_with_get(my_dict, "key") == "value"
    assert get_value_from_dict_with_get(my_dict, "key2") is None
    # assert default value
    assert (
        get_value_from_dict_with_get(my_dict, "key2", "default_value")
        == "default_value"
    )


def test_get_value_from_defaultdict():
    my_dict = {"key": "value"}
    assert get_value_from_defaultdict(my_dict, "key") == "value"
    assert get_value_from_defaultdict(my_dict, "key2") is None
    # assert default value
    assert get_value_from_defaultdict(my_dict, "key2", "default") == "default"
