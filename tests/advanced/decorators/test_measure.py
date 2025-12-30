from time import sleep

from advanced.decorators import measure


# Set decorated function to test
@measure
def sleeper(seconds: int):
    sleep(seconds)


def test_measure_sleeper_1(debug_caplog) -> None:
    sleeper(1)

    assert len(debug_caplog.records) == 1
    assert debug_caplog.records[0].levelname == "DEBUG"
    # As measure can take more than 1 second, we can't test the exact string
    assert debug_caplog.records[0].message.startswith(
        "Method sleeper executed in 1.00",
    )
    assert debug_caplog.records[0].message.endswith("seconds")
    assert debug_caplog.records[0].name == "advanced.decorators.measure"


def test_measure_sleeper_2(debug_caplog) -> None:
    sleeper(2)

    assert len(debug_caplog.records) == 1
    assert debug_caplog.records[0].levelname == "DEBUG"
    # As measure can take more than 1 second, we can't test the exact string
    assert debug_caplog.records[0].message.startswith(
        "Method sleeper executed in 2.00",
    )
    assert debug_caplog.records[0].message.endswith("seconds")
    assert debug_caplog.records[0].name == "advanced.decorators.measure"
