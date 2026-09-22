import logging

import pytest


@pytest.fixture(autouse=True)
def debug_caplog(caplog):
    caplog.set_level(logging.DEBUG)
    return caplog


class _Writer:
    """Callable recorder used to capture messages written during tests."""

    def __init__(self) -> None:
        self.written: list[str] = []

    def __call__(self, message: str) -> None:
        self.written.append(message)

    def read(self) -> str:
        return "".join(self.written)

    def clear(self) -> None:
        self.written.clear()


@pytest.fixture
def writer() -> _Writer:
    return _Writer()
