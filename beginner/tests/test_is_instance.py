from src.beginner.check_is_instance import is_instance


def test_is_instance():
    assert is_instance("instance", str)
    assert is_instance(33, int)
    assert is_instance(33, (int, str))
    assert is_instance(33.3, float)
    assert is_instance((1, 2, 3,), tuple)
    assert is_instance([1, 2, 3], list)
    assert is_instance({"key": "value"}, dict)
