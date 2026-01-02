import time

import pytest

from advanced.decorators import retry


def test_retry_default_params_ok(debug_caplog) -> None:
    # Set decorated function to test with default params
    @retry()
    def retry_ok():
        pass

    start_time = time.perf_counter()
    retry_ok()
    elapsed_time = time.perf_counter() - start_time

    log_records = debug_caplog.records
    assert len(log_records) == 1
    assert log_records[0].levelname == "DEBUG"
    assert log_records[0].message == "Attempt 1"
    assert log_records[0].name == "advanced.decorators.retry"

    assert elapsed_time < 0.2, (
        f"Expected less than 0.2s, got {elapsed_time:.2f}s"
    )


def test_retry_custom_params_ok(debug_caplog) -> None:
    # Set decorated function to test with custom params
    @retry(attempts=5, delay=0.1)
    def retry_ok():
        pass

    start_time = time.perf_counter()
    retry_ok()
    elapsed_time = time.perf_counter() - start_time

    log_records = debug_caplog.records
    assert len(log_records) == 1
    assert log_records[0].levelname == "DEBUG"
    assert log_records[0].message == "Attempt 1"
    assert log_records[0].name == "advanced.decorators.retry"

    assert elapsed_time < 0.2, (
        f"Expected less than 0.2s, got {elapsed_time:.2f}s"
    )


def test_retry_ko(debug_caplog) -> None:
    # Set decorated function to test with default params
    @retry()
    def retry_ko():
        raise Exception

    start_time = time.perf_counter()
    with pytest.raises(Exception):
        retry_ko()
    elapsed_time = time.perf_counter() - start_time

    log_records = debug_caplog.records
    assert len(log_records) == 6
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

    assert log_records[5].levelname == "ERROR"
    assert log_records[5].message == "Raising exception, max attempts reached"
    assert log_records[5].name == "advanced.decorators.retry"

    # Verify timing with 3 attempts and default delay. Backoff is incremental
    assert elapsed_time >= 6.0, f"Expected over 6.0s, got {elapsed_time:.2f}s"
    assert elapsed_time < 6.1, f"Expected down 6.1s, got {elapsed_time:.2f}s"
