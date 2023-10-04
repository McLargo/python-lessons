from src.beginner.check_is_instance import is_instance


def test_is_instance():
    assert is_instance("Hello World!", str) is True
    assert is_instance(b"Hello World!", bytes) is True
    assert is_instance(1, int) is True
    assert is_instance(1.0, float) is True
    assert is_instance(True, bool) is True
    assert is_instance([1, 2, 3], list) is True
    assert is_instance((1, 2, 3), tuple) is True
    assert is_instance({1, 2, 3}, set) is True
    assert is_instance({1: 1, 2: 2, 3: 3}, dict) is True
    assert is_instance(None, type(None)) is True


def test_is_instance_ko():
    assert is_instance("Hello World!", int) is False
    assert is_instance(b"Hello World!", str) is False
    assert is_instance(1, float) is False
    assert is_instance(1.0, int) is False
    assert is_instance(True, int) is False
    assert is_instance([1, 2, 3], tuple) is False
    assert is_instance((1, 2, 3), list) is False
    assert is_instance({1, 2, 3}, dict) is False
    assert is_instance({1: 1, 2: 2, 3: 3}, set) is False
    assert is_instance(None, int) is False
