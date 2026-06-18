"""Module to show inheritance.

This module contains an abstract class and 2 subclasses to show inheritance
with abstractmethod.

"""

import datetime
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Driver(ABC):
    """This is a driver, an abstract class that represents a driver."""

    novel_years: int = 0
    metric_unit: str = ""
    license_valid_from: datetime.date | None = None

    def is_novel(self) -> bool:
        """Return whatever the driver is novel or not.

        Returns:
            is_novel: True if the driver is novel, False otherwise.
        """
        if self.license_valid_from is None:
            return False

        novel_days: int = 365 * self.novel_years
        novel_until: datetime.date = (
            self.license_valid_from + datetime.timedelta(days=novel_days)
        )
        return (
            novel_until
            >= datetime.datetime.now(
                tz=datetime.timezone.utc,
            ).date()
        )

    @abstractmethod
    def speed_limit(self) -> str:
        """Return the speed limit with metic unit for the driver.

        It is an abstract method, must be implemented by subclasses.

        Returns:
            speed_limit: speed limit with metric unit for driver.
        """
        raise NotImplementedError


@dataclass
class UsaDriver(Driver):
    """Concrete class of a Driver that can drive in USA."""

    novel_years: int = 2
    metric_unit: str = "mph"

    def speed_limit(self) -> str:
        """Return the speed limit with metic unit for the driver.

        Returns:
            speed_limit: speed limit with metric unit for driver.
        """
        return f"70{self.metric_unit}"


@dataclass
class SpainDriver(Driver):
    """Concrete class of a Driver that can drive in Spain."""

    novel_years: int = 1
    metric_unit: str = "km/h"

    def speed_limit(self) -> str:
        """Return the speed limit with metic unit for the driver.

        Returns:
            speed_limit: speed limit with metric unit for driver.
        """
        if self.is_novel():
            return f"100{self.metric_unit}"
        return f"120{self.metric_unit}"
