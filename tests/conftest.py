import logging

import pytest


@pytest.fixture(autouse=True)
def debug_caplog(caplog):
    caplog.set_level(logging.DEBUG)
    return caplog


@pytest.fixture
def writer():
    def w(message):
        w.written.append(message)

    w.written = []
    w.read = lambda: "".join(w.written)
    w.clear = lambda: w.written.clear()

    return w
