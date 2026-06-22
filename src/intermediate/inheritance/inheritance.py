"""Module to show inheritance.

This module contains an abstract class and 2 subclasses to show inheritance
with abstractmethod.

"""

import datetime
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Driver(ABC):
    """Abstract base class representing a driver with licensing.

    This abstract class demonstrates inheritance patterns in Python using the
    ABC (Abstract Base Class) module. It defines common attributes and methods
    for all drivers while requiring subclasses to implement specific behavior
    through the abstract speed_limit method.

    The class combines dataclass and ABC features to provide both automatic
    initialization and abstract method enforcement.

    Attributes:
        novel_years: Number of years after license issuance during which the
            driver is considered "novel" or inexperienced. Defaults to 0.
        metric_unit: Unit of speed measurement (e.g., 'mph' or 'km/h').
            Defaults to empty string.
        license_valid_from: Date when the driver's license was issued. Used
            to calculate novel status. None if date is unknown.
    """

    novel_years: int = 0
    metric_unit: str = ""
    license_valid_from: datetime.date | None = None

    def is_novel(self) -> bool:
        """Determine if the driver is in their "novel" period.

        A driver is considered novel if less time has passed since their license
        was issued than the configured novel_years period. This is commonly used
        to apply stricter rules for new drivers.

        Returns:
            True if the driver is within their novel period (inexperienced),
            False if they are experienced or if license_valid_from is None.
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
        """Return the speed limit with metric unit for this driver type.

        This is an abstract method that must be implemented by all concrete
        subclasses. Each subclass defines its own speed limit rules based on
        local regulations and driver experience level.

        Returns:
            A string representing the speed limit with its unit (e.g., "70mph",
            "120km/h").

        Raises:
            NotImplementedError: If a subclass fails to implement this method.
        """
        raise NotImplementedError


@dataclass
class UsaDriver(Driver):
    """Concrete Driver implementation for USA driving regulations.

    This class inherits from Driver and implements USA-specific driving
    rules. In the USA, novel drivers have a 2-year period and speeds
    are measured in miles per hour (mph).

    Attributes:
        novel_years: Set to 2 years for USA drivers.
        metric_unit: Set to "mph" (miles per hour) for USA.
    """

    novel_years: int = 2
    metric_unit: str = "mph"

    def speed_limit(self) -> str:
        """Return the standard highway speed limit for USA drivers.

        USA drivers have a fixed highway speed limit of 70mph regardless
        of their novel status. This demonstrates how subclasses can
        implement abstract methods with their own logic.

        Returns:
            String representing the speed limit: "70mph".
        """
        return f"70{self.metric_unit}"


@dataclass
class SpainDriver(Driver):
    """Concrete Driver implementation for Spanish driving regulations.

    This class inherits from Driver and implements Spain-specific driving
    rules. In Spain, novel drivers have a 1-year period with reduced speed
    limits, and speeds are measured in kilometers per hour (km/h).

    Attributes:
        novel_years: Set to 1 year for Spanish drivers.
        metric_unit: Set to "km/h" (kilometers per hour) for Spain.
    """

    novel_years: int = 1
    metric_unit: str = "km/h"

    def speed_limit(self) -> str:
        """Return the highway speed limit based on driver experience.

        Spanish driving regulations enforce different speed limits for novel
        (inexperienced) and experienced drivers. Novel drivers are limited
        to 100km/h while experienced drivers can drive at 120km/h on highways.
        This demonstrates how subclasses can use inherited methods (is_novel)
        to implement their own logic.

        Returns:
            String representing the speed limit: "100km/h" for novel drivers
            or "120km/h" for experienced drivers.
        """
        if self.is_novel():
            return f"100{self.metric_unit}"
        return f"120{self.metric_unit}"
