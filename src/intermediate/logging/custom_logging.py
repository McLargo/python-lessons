"""Module to show the use of logging libraries.

This module contains different logging libraries, how to initialize, configure
and use.

"""

import logging
import sys

from loguru import logger as logger_loguru


def default_logging(level: int):
    """Example of default logging configuration with basic usage.

    Shows how to use Python's built-in logging module without custom
    configuration. Logs messages at all severity levels to demonstrate
    the default output format.

    Args:
        level: The logging level to set. Must be one of the standard
            logging levels: DEBUG (10), INFO (20), WARNING (30), ERROR (40),
            or CRITICAL (50).

    Raises:
        IndexError: If the provided level is not a valid logging level.
    """
    if level not in logging._levelToName:
        raise IndexError("Invalid level to set logging.")

    logging.debug("DEBUG logging")
    logging.info("INFO logging")
    logging.warning("WARNING logging")
    logging.error("ERROR logging")
    logging.critical("CRITICAL logging")


def custom_logging_format(format: str, datefmt: str):
    """Example of custom logging format and date format configuration.

    Shows how to customize the logging output by specifying a format
    string for the log message and a date format string. Additional
    configuration options like filename and filemode can be used with
    basicConfig to write logs to files.

    Args:
        format: Format string for log messages. Can include fields like
            %(levelname)s, %(message)s, %(asctime)s, etc.
        datefmt: Format string for timestamps using time.strftime() format
            codes (e.g., '%Y-%m-%d %H:%M:%S').

    Note:
        Additional basicConfig parameters:
        - filename: File path for logging with FileHandler
        - filemode: Mode to open the log file (e.g., 'a' for append)
    """
    logging.basicConfig(
        level=logging.INFO,
        format=format,
        datefmt=datefmt,
    )
    logger = logging.getLogger(__name__)

    logger.info("INFO logging formatted")


def lazy_logging_format():
    """Example of lazy logging format.

    Avoid using concatenation or f-strings in logging calls. This function
    demonstrates how to use lazy formatting in logging, where the log message is
    formatted only if the message is actually going to be logged. This can
    improve performance when logging is disabled for certain levels.
    """
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    logger.info("Using lazy formatting: %s", "INFO logging formatted")


def default_loguru():
    """Example of default loguru configuration with basic usage.

    Shows how to use the loguru library without custom configuration.
    Loguru provides colorized output, better formatting, and easier
    configuration compared to the standard logging module. Logs messages
    at all severity levels to demonstrate the default output.
    """
    logger_loguru.debug("DEBUG loguru")
    logger_loguru.info("INFO loguru")
    logger_loguru.warning("WARNING loguru")
    logger_loguru.error("ERROR loguru")
    logger_loguru.critical("CRITICAL loguru")


def custom_loguru_format_and_level(format: str, level: str):
    """Example of custom loguru configuration with format and level.

    Shows how to add a custom sink to loguru with specific formatting
    and log level. Loguru uses the add() method to configure where logs
    go (sink) and how they are formatted. Sinks can be stdout, files,
    or custom handlers.

    Args:
        format: Format string for log messages. Can include fields like
            {level}, {message}, {time}, {name}, etc. Uses Python's
            string formatting syntax.
        level: Minimum log level as a string (e.g., 'DEBUG', 'INFO',
            'WARNING', 'ERROR', 'CRITICAL').

    Note:
        The sink parameter in logger.add() can be:
        - sys.stdout or sys.stderr for console output
        - A file path string for file logging
        - A logging.Handler instance for custom handling

        For more information, see:
        https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.add
    """
    logger_loguru.add(sys.stdout, format=format, level=level)

    logger_loguru.debug("DEBUG loguru formatted")
    logger_loguru.info("INFO loguru formatted")
    logger_loguru.warning("WARNING loguru formatted")
    logger_loguru.error("ERROR loguru formatted")
    logger_loguru.critical("CRITICAL loguru formatted")
