import pytest

from intermediate.exceptions import (
    CustomError,
    exception_controlled,
    exception_controlled_raise_custom_exception,
    exception_controlled_raise_exception,
    exception_uncontrolled,
    exception_with_finally,
)


def test_exception_uncontrolled() -> None:
    with pytest.raises(TypeError) as exc:
        exception_uncontrolled()

    assert (
        str(exc.value) == "unsupported operand type(s) for +: 'int' and 'str'"
    )


def test_exception_controlled(debug_caplog) -> None:
    exception_controlled()

    assert len(debug_caplog.records) == 1
    assert debug_caplog.records[0].levelname == "WARNING"
    assert debug_caplog.records[0].message == (
        "Cannot sum int + string. Continue."
    )


def test_exception_controlled_raise_exception(debug_caplog) -> None:
    with pytest.raises(TypeError) as exc:
        exception_controlled_raise_exception()

    exception_message = "unsupported operand type(s) for +: 'int' and 'str'"
    assert str(exc.value) == exception_message

    assert len(debug_caplog.records) == 1
    assert debug_caplog.records[0].levelname == "ERROR"
    assert debug_caplog.records[0].message == (
        "Cannot sum int + string. Raising TypeError."
    )


def test_exception_controlled_raise_custom_exception(debug_caplog) -> None:
    with pytest.raises(CustomError) as exc:
        exception_controlled_raise_custom_exception()

    assert exc.value.message == "Controlled TypeError"
    assert isinstance(exc.value.exception, TypeError)

    assert len(debug_caplog.records) == 1
    assert debug_caplog.records[0].levelname == "ERROR"
    assert debug_caplog.records[0].message == (
        "Cannot sum int + string. Raising CustomError."
    )


def test_exception_with_finally_raise_exception_false(debug_caplog) -> None:
    exception_with_finally(raise_exception=False)

    assert len(debug_caplog.records) == 1
    assert debug_caplog.records[0].levelname == "DEBUG"
    assert debug_caplog.records[0].message == "Finally is executed."


def test_exception_with_finally_raise_exception_true(debug_caplog) -> None:
    with pytest.raises(TypeError) as exc:
        exception_with_finally(raise_exception=True)

    exception_message = "unsupported operand type(s) for +: 'int' and 'str'"
    assert str(exc.value) == exception_message

    assert len(debug_caplog.records) == 2
    assert debug_caplog.records[0].levelname == "ERROR"
    assert debug_caplog.records[0].message == (
        "Cannot sum int + string. Raising TypeError."
    )

    assert debug_caplog.records[1].levelname == "DEBUG"
    assert debug_caplog.records[1].message == "Finally is executed."
