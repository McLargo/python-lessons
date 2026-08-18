from collections import defaultdict

import pytest
from hypothesis import given
from hypothesis import strategies as st

from beginner.dict_vs_defaultdict import (
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


@pytest.mark.parametrize(
    ("mapping", "key", "expected"),
    [
        ({"a": "1"}, "a", "1"),
        ({"a": "1", "b": "2"}, "b", "2"),
        ({"only": "value"}, "only", "value"),
    ],
)
def test_all_access_styles_agree_on_present_keys(mapping, key, expected):
    # For a key that is present, all three access styles must return the
    # same value; they only differ in how they handle missing keys.
    assert get_value_from_dict_with_square_brackets(mapping, key) == expected
    assert get_value_from_dict_with_get(mapping, key) == expected
    assert get_value_from_defaultdict(mapping, key) == expected


@pytest.mark.parametrize(
    ("mapping", "missing_key", "default"),
    [
        ({"a": "1"}, "b", "fallback"),
        ({"a": "1", "b": "2"}, "c", "other"),
        ({}, "anything", "default"),
    ],
)
def test_get_and_defaultdict_return_default_for_missing_keys(
    mapping,
    missing_key,
    default,
):
    # `get` and `defaultdict` both provide a safe path for missing keys,
    # whereas square-bracket access raises KeyError.
    assert (
        get_value_from_dict_with_get(mapping, missing_key, default) == default
    )
    assert get_value_from_defaultdict(mapping, missing_key, default) == default
    with pytest.raises(KeyError):
        get_value_from_dict_with_square_brackets(mapping, missing_key)


def test_defaultdict_mutates_the_container():
    # Pitfall: reading a missing key from a defaultdict INSERTS an entry
    # produced by the default_factory. A plain dict would not mutate on
    # read; a defaultdict does.
    dd: defaultdict[str, list[int]] = defaultdict(list)

    assert "missing" not in dd

    # Read-only access on a missing key silently creates a new entry.
    _ = dd["missing"]

    assert "missing" in dd
    assert dd["missing"] == []
    assert len(dd) == 1


def test_plain_dict_get_does_not_mutate():
    # Contrast: `dict.get` never mutates the dictionary, even when the key
    # is missing. This is the safe alternative to the pitfall shown above.
    plain: dict[str, str] = {"a": "1"}

    assert (
        get_value_from_dict_with_get(plain, "missing", "fallback") == "fallback"
    )

    assert "missing" not in plain
    assert plain == {"a": "1"}


def test_get_value_from_defaultdict_does_not_mutate_input_dict():
    # The helper builds a fresh defaultdict internally, so the caller's
    # original dict is never mutated even when a missing key is queried.
    original = {"a": "1"}
    snapshot = dict(original)

    get_value_from_defaultdict(original, "not_there", "x")

    assert original == snapshot


@given(
    key=st.text(min_size=1, max_size=10),
    value=st.text(),
    default=st.text(),
)
def test_get_returns_default_for_any_missing_key(key, value, default):
    # For any key that is definitely absent, `get` must return the caller
    # provided default and never raise.
    mapping = {key: value}
    missing_key = key + "_missing"

    assert (
        get_value_from_dict_with_get(mapping, missing_key, default) == default
    )
    assert get_value_from_defaultdict(mapping, missing_key, default) == default
