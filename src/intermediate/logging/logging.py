"""Module to show the use of logging libraries.

This module contains different logging libraries, how to initialize, configure
and use.

"""
import logging
import sys

from loguru import logger as logger_loguru


def default_logging(level: int):
    """Method to show default logging configuration.

    Args:
        level (int): level to set in logging
    """
    if level not in logging._levelToName:
        raise IndexError("Invalid level to set logging.")

    logging.debug("DEBUG logging")
    logging.info("INFO logging")
    logging.warning("WARNING logging")
    logging.error("ERROR logging")
    logging.critical("CRITICAL logging")


def custom_logging_format(format: str, datefmt: str):
    """Method to show logging configuration format.

    Other arguments worthy to mention are:
    filename: using the path as log file with FileHandler.
    filemode: specifies the mode to open the log file.
    """
    logging.basicConfig(
        level=logging.INFO,
        format=format,
        datefmt=datefmt,
    )
    logger = logging.getLogger(__name__)

    logger.info("INFO logging formatted")


def default_loguru():
    """Method to show default loguru configuration."""
    logger_loguru.debug("DEBUG loguru")
    logger_loguru.info("INFO loguru")
    logger_loguru.warning("WARNING loguru")
    logger_loguru.error("ERROR loguru")
    logger_loguru.critical("CRITICAL loguru")


def custom_loguru_format_and_level(format: str, level: str):
    """Method to show loguru custom configuration.

    Add custom configuration to loguru, such as format and level.
    Sink is the first argument, representing how/where to log.
    It can be sys.*, or a log file path or a loggingHandler.

    More information in the official loguru documentation:
    https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.add
    """
    logger_loguru.add(sys.stdout, format=format, level=level)

    logger_loguru.debug("DEBUG loguru formatted")
    logger_loguru.info("INFO loguru formatted")
    logger_loguru.warning("WARNING loguru formatted")
    logger_loguru.error("ERROR loguru formatted")
    logger_loguru.critical("CRITICAL loguru formatted")
