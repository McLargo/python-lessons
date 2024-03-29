import logging

import pytest


@pytest.fixture(autouse=True)
def debug_caplog(caplog):
    caplog.set_level(logging.DEBUG)
    return caplog
