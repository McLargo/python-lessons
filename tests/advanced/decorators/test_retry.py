import pytest

from advanced.decorators import retry


def test_retry_ok(debug_caplog) -> None:
    # Set decorated function to test
    @retry()
    def retry_ok():
        pass

    retry_ok()

    log_records = debug_caplog.records
    assert len(log_records) == 1
    assert log_records[0].levelname == "DEBUG"
    assert log_records[0].message == "Attempt 1"
    assert log_records[0].name == "advanced.decorators.retry"


def test_retry_ko(debug_caplog) -> None:
    # Set decorated function to test
    @retry(attempts=5, delay=0.1)
    def retry_ko():
        raise Exception

    with pytest.raises(Exception):
        retry_ko()

    log_records = debug_caplog.records
    assert len(log_records) == 10
    assert log_records[0].levelname == "DEBUG"
    assert log_records[0].message == "Attempt 1"
    assert log_records[0].name == "advanced.decorators.retry"

    assert log_records[1].levelname == "WARNING"
    assert log_records[1].message == "Exception, retrying"
    assert log_records[1].name == "advanced.decorators.retry"

    assert log_records[2].levelname == "DEBUG"
    assert log_records[2].message == "Attempt 2"
    assert log_records[2].name == "advanced.decorators.retry"

    assert log_records[3].levelname == "WARNING"
    assert log_records[3].message == "Exception, retrying"
    assert log_records[3].name == "advanced.decorators.retry"

    assert log_records[4].levelname == "DEBUG"
    assert log_records[4].message == "Attempt 3"
    assert log_records[4].name == "advanced.decorators.retry"

    assert log_records[5].levelname == "WARNING"
    assert log_records[5].message == "Exception, retrying"
    assert log_records[5].name == "advanced.decorators.retry"

    assert log_records[6].levelname == "DEBUG"
    assert log_records[6].message == "Attempt 4"
    assert log_records[6].name == "advanced.decorators.retry"

    assert log_records[7].levelname == "WARNING"
    assert log_records[7].message == "Exception, retrying"
    assert log_records[7].name == "advanced.decorators.retry"

    assert log_records[8].levelname == "DEBUG"
    assert log_records[8].message == "Attempt 5"
    assert log_records[8].name == "advanced.decorators.retry"

    assert log_records[9].levelname == "ERROR"
    assert log_records[9].message == "Raising exception, max attempts reached"
    assert log_records[9].name == "advanced.decorators.retry"
