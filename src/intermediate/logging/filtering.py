"""Custom logging filter to mask sensitive information in log records."""

import logging
import re
from logging import LogRecord


class CustomFilter(logging.Filter):
    """Custom logging filter to mask sensitive information in log records.

    This filter extends logging.Filter to automatically detect and mask
    sensitive information such as passwords and email addresses in log
    records. It uses regular expressions to identify sensitive data and
    applies appropriate masking functions.

    Attributes:
        keys_to_mask: Dictionary mapping attribute names to their masking
            configuration. Each configuration contains a regex pattern and
            the name of the masking function to apply.
    """

    keys_to_mask = {
        "email": {
            "pattern": r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
            "mask_func": "mask_email",
        },
        "password": {
            "pattern": r".+",
            "mask_func": "mask_password",
        },
    }

    def filter(self, record: LogRecord) -> bool:
        """Override filter method to mask sensitive information.

        Iterates through all attributes in the log record and applies masking
        to any attributes that match keys in keys_to_mask. The masking uses
        regex patterns to identify sensitive data and applies the configured
        masking function.

        Args:
            record: The LogRecord instance to filter and potentially modify.
                Contains all information about the log event including message,
                level, and custom attributes.

        Returns:
            Always returns True to indicate the record should be logged.
            The record may be modified in-place with masked values.
        """
        for key in record.__dict__.keys():
            if key in self.keys_to_mask:
                if isinstance(record.__dict__[key], str):
                    config = self.keys_to_mask[key]
                    mask_func = getattr(self, config["mask_func"])
                    record.__dict__[key] = re.sub(
                        config["pattern"],
                        mask_func,
                        record.__dict__[key],
                    )
        return True

    def mask_password(self, match_obj: re.Match) -> str:
        """Mask password completely with asterisks.

        Replaces the entire password with asterisks, with the masked
        string having the same length as the original password. This
        provides complete concealment while preserving information about
        password length.

        Args:
            match_obj: Regular expression match object containing the
                password string to mask.

        Returns:
            String of asterisks with length equal to the original password.
        """
        return "*" * len(match_obj.group(0))

    def mask_email(self, match_obj: re.Match) -> str:
        """Mask email address local part while keeping domain visible.

        Replaces the entire local part (before @) with asterisks while
        keeping the domain visible. This provides some privacy while
        maintaining context about the email domain.

        Args:
            match_obj: Regular expression match object containing the
                email address to mask.

        Returns:
            Masked email string in format '*****@domain.com' where the
            number of asterisks matches the length of the original local part.
        """
        local_part, domain = match_obj.group(0).split("@")
        masked_local = "*" * (len(local_part))
        return f"{masked_local}@{domain}"
