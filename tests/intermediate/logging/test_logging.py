import datetime
import logging
import re

import pytest
from loguru import logger as logger_loguru
from src.intermediate.logging import (
    custom_logging_format,
    custom_loguru_format_and_level,
    default_logging,
    default_loguru,
)


def test_default_logging_level_not_present():
    with pytest.raises(IndexError):
        default_logging(level=100)


@pytest.mark.parametrize(
    "level, total_logs",
    [
        (logging.DEBUG, 5),
        (logging.INFO, 4),
        (logging.WARNING, 3),
        (logging.WARN, 3),
        (logging.ERROR, 2),
        (logging.CRITICAL, 1),
    ],
)
def test_default_logging(level, total_logs, caplog):
    # set level to caplog
    caplog.set_level(level)

    default_logging(level=level)

    assert len(caplog.records) == total_logs


def test_custom_logging_configuration_format(caplog):
    format: str = "%(asctime)s | %(levelname)s | %(message)s"
    date_format: str = "%Y-%m-%dT%H:%M:%S"

    # set formatter to caplog
    formatter = logging.Formatter(
        fmt=format,
        datefmt=date_format,
    )
    caplog.handler.setFormatter(formatter)

    custom_logging_format(format=format, datefmt=date_format)

    assert len(caplog.records) == 1

    assert (
        re.search(
            "^[\\d,-|T]{1,19} \\| INFO \\| INFO logging formatted",
            caplog.text,
        )
        is not None
    )

    assert caplog.records[0].message == "INFO logging formatted"
    assert caplog.records[0].name == "src.intermediate.logging.logging"
    assert datetime.datetime.strptime(  # noqa: DTZ007
        caplog.records[0].asctime,
        date_format,
    )


def test_default_loguru(writer):
    # add writer to logger_loguru to be able to capture logs
    logger_loguru.add(writer)
    default_loguru()

    assert len(writer.written) == 5

    assert re.search("\\| DEBUG    \\|", writer.written[0]) is not None
    assert re.search("DEBUG loguru\\\n$", writer.written[0]) is not None

    assert re.search("\\| INFO     \\|", writer.written[1]) is not None
    assert re.search("INFO loguru\\\n$", writer.written[1]) is not None

    assert re.search("\\| WARNING  \\|", writer.written[2]) is not None
    assert re.search("WARNING loguru\\\n$", writer.written[2]) is not None

    assert re.search("\\| ERROR    \\|", writer.written[3]) is not None
    assert re.search("ERROR loguru\\\n$", writer.written[3]) is not None

    assert re.search("\\| CRITICAL \\|", writer.written[4]) is not None
    assert re.search("CRITICAL loguru\\\n$", writer.written[4]) is not None


def test_custom_loguru_format(writer):
    format: str = "{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}"
    level: str = "WARNING"

    # add writer to logger_loguru to be able to capture logs
    logger_loguru.add(writer, format=format, level=level)
    custom_loguru_format_and_level(format=format, level=level)

    assert len(writer.written) == 3

    regex_date_format: str = "^[\\d,-]{1,10} at [\\d,:]{8}"
    assert re.search(regex_date_format, writer.written[0]) is not None
    assert re.search("\\| WARNING \\|", writer.written[0]) is not None
    assert (
        re.search(
            "WARNING loguru formatted\\\n$",
            writer.written[0],
        )
        is not None
    )

    assert re.search(regex_date_format, writer.written[1]) is not None
    assert re.search("\\| ERROR \\|", writer.written[1]) is not None
    assert (
        re.search(
            "ERROR loguru formatted\\\n$",
            writer.written[1],
        )
        is not None
    )

    assert re.search(regex_date_format, writer.written[2]) is not None
    assert re.search("\\| CRITICAL \\|", writer.written[2]) is not None
    assert (
        re.search(
            "CRITICAL loguru formatted\\\n$",
            writer.written[2],
        )
        is not None
    )
