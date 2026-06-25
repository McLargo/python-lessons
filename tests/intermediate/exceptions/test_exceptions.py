import pytest
from hypothesis import given
from hypothesis import strategies as st

from intermediate.exceptions import (
    CustomError,
    exception_controlled,
    exception_controlled_raise_custom_exception,
    exception_controlled_raise_exception,
    exception_uncontrolled,
    exception_with_else,
    exception_with_finally,
    multiple_exceptions_controlled,
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


def test_custom_error_str_with_exception() -> None:
    """Test CustomError string representation includes cause information."""
    exc = TypeError("test")
    custom_error = CustomError(message="An error occurred", exception=exc)

    error_str = str(custom_error)
    assert "An error occurred" in error_str
    assert "TypeError" in error_str
    assert "test" in error_str


def test_custom_error_str_without_exception() -> None:
    """Test CustomError string representation when exception is None."""
    custom_error = CustomError(message="An error occurred", exception=None)

    error_str = str(custom_error)
    assert error_str == "An error occurred"


def test_exception_controlled_raise_custom_exception(
    debug_caplog,
) -> None:
    """Test that any int + str always raises TypeError."""
    with pytest.raises(CustomError) as exc:
        exception_controlled_raise_custom_exception()

    assert exc.value.message == "Controlled TypeError"
    assert isinstance(exc.value.exception, TypeError)

    assert len(debug_caplog.records) == 1
    assert debug_caplog.records[0].levelname == "ERROR"
    assert debug_caplog.records[0].message == (
        "Cannot sum int + string. Raising CustomError."
    )


@given(
    value1=st.integers(),
    value2=st.text(min_size=1),
)
def test_exception_controlled_raise_custom_exception_with_hypothesis(
    value1: int,
    value2: str,
) -> None:
    """Test that any int + str always raises TypeError."""
    with pytest.raises(CustomError) as exc:
        exception_controlled_raise_custom_exception(number=value1, char=value2)

    assert exc.value.message == "Controlled TypeError"
    assert isinstance(exc.value.exception, TypeError)


@given(
    message=st.text(min_size=1, max_size=1000),
    original_exc=st.sampled_from(
        [
            TypeError("test"),
            ValueError("test"),
            KeyError("test"),
            AttributeError("test"),
        ],
    ),
)
def test_custom_error_properties(message: str, original_exc: Exception) -> None:
    """Test CustomError correctly wraps any exception with any message."""
    error = CustomError(message=message, exception=original_exc)

    assert error.message == message
    assert error.exception is original_exc
    assert isinstance(error, Exception)


@given(
    message=st.one_of(
        st.text(min_size=0, max_size=0),
        st.text(min_size=100),
        st.just(""),
        st.text(alphabet=st.characters(blacklist_categories=("Cs",))),
    ),
)
def test_custom_error_handles_edge_case_messages(message: str) -> None:
    """Test CustomError handles edge case messages correctly."""
    exc = ValueError("test")
    error = CustomError(message=message, exception=exc)

    assert error.message == message
    assert error.exception is exc


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


def test_exception_with_else_raise_exception_false(debug_caplog) -> None:
    exception_with_else(raise_exception=False)

    assert len(debug_caplog.records) == 1
    assert debug_caplog.records[0].levelname == "DEBUG"
    assert debug_caplog.records[0].message == "Else is executed."


def test_exception_with_else_raise_exception_true(debug_caplog) -> None:
    with pytest.raises(TypeError) as exc:
        exception_with_else(raise_exception=True)

    exception_message = "unsupported operand type(s) for +: 'int' and 'str'"
    assert str(exc.value) == exception_message

    assert len(debug_caplog.records) == 1
    assert debug_caplog.records[0].levelname == "ERROR"
    assert debug_caplog.records[0].message == (
        "Cannot sum int + string. Raising TypeError."
    )


def test_multiple_exceptions_controlled_type_error(debug_caplog) -> None:
    with pytest.raises(TypeError) as exc:
        multiple_exceptions_controlled(type_error=True)

    exception_message = "unsupported operand type(s) for +: 'int' and 'str'"
    assert str(exc.value) == exception_message

    assert len(debug_caplog.records) == 1
    assert debug_caplog.records[0].levelname == "ERROR"
    assert debug_caplog.records[0].message == (
        "An error occurred: unsupported operand type(s) for +: "
        + "'int' and 'str'. Raising the exception."
    )


def test_multiple_exceptions_controlled_value_error(debug_caplog) -> None:
    with pytest.raises(ValueError) as exc:
        multiple_exceptions_controlled(type_error=False)

    exception_message = "invalid literal for int() with base 10: 'a'"
    assert str(exc.value) == exception_message

    assert len(debug_caplog.records) == 1
    assert debug_caplog.records[0].levelname == "ERROR"
    assert debug_caplog.records[0].message == (
        "An error occurred: invalid literal for int() with base 10: 'a'. "
        + "Raising the exception."
    )
