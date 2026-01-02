import re
from time import sleep

from advanced.decorators import measure


def test_measure_sleeper_1(debug_caplog) -> None:
    # Set decorated function to test
    @measure
    def sleeper(seconds: int):
        sleep(seconds)

    sleeper(1)

    assert len(debug_caplog.records) == 1
    assert debug_caplog.records[0].levelname == "DEBUG"
    # Verify message format with regex
    message = debug_caplog.records[0].message
    pattern = r"^Method sleeper executed in 1\.\d+ seconds$"
    assert re.match(pattern, message), f"Message '{message}' doesn't match"
    assert debug_caplog.records[0].name == "advanced.decorators.measure"


def test_measure_sleeper_2(debug_caplog) -> None:
    # Set decorated function to test
    @measure
    def sleeper(seconds: int):
        sleep(seconds)

    sleeper(2)

    assert len(debug_caplog.records) == 1
    assert debug_caplog.records[0].levelname == "DEBUG"
    # Verify message format with regex
    message = debug_caplog.records[0].message
    pattern = r"^Method sleeper executed in 2\.\d+ seconds$"
    assert re.match(pattern, message), f"Message '{message}' doesn't match"

    assert debug_caplog.records[0].name == "advanced.decorators.measure"
