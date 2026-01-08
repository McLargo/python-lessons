from hypothesis import given
from hypothesis import strategies as st
from src.beginner.check_is_instance import is_instance


@given(st.integers())
def test_is_instance_int(n):
    assert is_instance(n, int) is True
    assert is_instance(n, str) is False


@given(st.text())
def test_is_instance_str(s):
    assert is_instance(s, str) is True
    assert is_instance(s, int) is False


@given(st.lists(st.integers()))
def test_is_instance_list(lst):
    assert is_instance(lst, list) is True
    assert is_instance(lst, dict) is False


@given(st.tuples(st.integers()))
def test_is_instance_tuple(tpl):
    assert is_instance(tpl, tuple) is True
    assert is_instance(tpl, list) is False


@given(st.dictionaries(st.text(), st.integers()))
def test_is_instance_dict(dct):
    assert is_instance(dct, dict) is True
    assert is_instance(dct, list) is False


@given(st.sets(st.integers()))
def test_is_instance_set(st_set):
    assert is_instance(st_set, set) is True
    assert is_instance(st_set, list) is False


@given(st.floats())
def test_is_instance_float(flt):
    assert is_instance(flt, float) is True
    assert is_instance(flt, int) is False


@given(st.booleans())
def test_is_instance_bool(bol):
    assert is_instance(bol, bool) is True
    assert is_instance(bol, str) is False


@given(st.binary())
def test_is_instance_bytes(bts):
    assert is_instance(bts, bytes) is True
    assert is_instance(bts, str) is False


@given(st.none())
def test_is_instance_none(none_val):
    assert is_instance(none_val, type(None)) is True
    assert is_instance(None, int) is False
