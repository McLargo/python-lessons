"""Custom logging filter to mask sensitive information in log records."""

import logging
import re
from logging import LogRecord


class CustomFilter(logging.Filter):
    """Custom logging filter to mask sensitive information in log records."""

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

        You can mask sensitive data in record attributes.
        Also, you can mask record msg or arguments,
        but only by regex/exact match..
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

    def mask_password(self, match_obj):
        """Mask password completely."""
        return "*" * len(match_obj.group(0))

    def mask_email(self, match_obj):
        """Mask email address, showing only first character before @."""
        local_part, domain = match_obj.group(0).split("@")
        masked_local = "*" * (len(local_part))
        return f"{masked_local}@{domain}"
