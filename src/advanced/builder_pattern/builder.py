"""Builder pattern example in Python.

This module showcases the Builder pattern with two meaningfully different
implementations: EconomyTripBuilder and LuxuryTripBuilder. Each builder
enforces different business rules and defaults appropriate for its trip type.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field


class TripType:
    """Class representing different types of trips."""

    ECONOMY = "Economy"
    LUXURY = "Luxury"


@dataclass
class Trip:
    """Class representing a trip with customizable attributes and amenities.

    This class serves as the product in the Builder pattern, constructed
    step-by-step by different builder implementations.

    Attributes:
        name: The name/title of the trip.
        destination: The destination location.
        passengers: List of passenger names.
        minimum_budget: Minimum budget for the trip.
        maximum_budget: Maximum budget for the trip.
        type: Type of trip (Economy or Luxury).
        amenities: List of included amenities/services.
    """

    name: str = ""
    destination: str = ""
    passengers: list[str] = field(default_factory=list)
    minimum_budget: float = 0.0
    maximum_budget: float = 0.0
    type: str = TripType.ECONOMY
    amenities: list[str] = field(default_factory=list)

    def __str__(self) -> str:
        """Return a string representation of the trip."""
        return (
            f"{self.type} trip: {self.name}, "
            f"destination: {self.destination}, "
            f"passengers: {len(self.passengers)}, "
            f"budget: {self.minimum_budget}-{self.maximum_budget}, "
            f"amenities: {', '.join(self.amenities) if self.amenities else '-'}"
        )


class TripBuilder(ABC):
    """Abstract base class for trip builders in the builder pattern.

    This interface defines the contract that all concrete trip builders must
    implement. Different builders can enforce different business rules and
    validation logic appropriate for their trip type.

    Each method should handle setting properties with appropriate validation
    and default behavior for the specific builder type.
    """

    @abstractmethod
    def set_name(self, name: str) -> "TripBuilder":
        """Set the name of the trip.

        Args:
            name: The name to set for the trip.

        Returns:
            Self for method chaining.
        """
        pass

    @abstractmethod
    def set_destination(self, destination: str) -> "TripBuilder":
        """Set the destination of the trip.

        Args:
            destination: The destination to set for the trip.

        Returns:
            Self for method chaining.
        """
        pass

    @abstractmethod
    def set_passengers(self, passengers: list[str]) -> "TripBuilder":
        """Set the passengers for the trip.

        Args:
            passengers: The list of passengers to set for the trip.

        Returns:
            Self for method chaining.

        Raises:
            ValueError: If passenger list violates builder-specific constraints.
        """
        pass

    @abstractmethod
    def set_budget(
        self,
        minimum_budget: float,
        maximum_budget: float,
    ) -> "TripBuilder":
        """Set the minimum and maximum budget for the trip.

        Args:
            minimum_budget: The minimum budget for the trip.
            maximum_budget: The maximum budget for the trip.

        Returns:
            Self for method chaining.

        Raises:
            ValueError: If budget violates builder-specific constraints.
        """
        pass

    @abstractmethod
    def build(self) -> Trip:
        """Construct and return the final Trip object.

        Returns:
            The constructed Trip instance.
        """
        pass


class EconomyTripBuilder(TripBuilder):
    """Concrete builder for creating economy trips.

    Economy trips are budget-conscious with the following characteristics:
    - Maximum budget capped at 1000 per person
    - No passenger limit (group-friendly)
    - Basic amenities included
    - Suitable for budget travelers and large groups
    """

    # Class constants for validation
    MAX_BUDGET_PER_PERSON = 1000.0
    DEFAULT_AMENITIES = ["Standard accommodation", "Group transport"]

    def __init__(self) -> None:
        """Initialize a new EconomyTripBuilder with default amenities."""
        self.trip = Trip(
            type=TripType.ECONOMY,
            amenities=self.DEFAULT_AMENITIES.copy(),
        )

    def set_name(self, name: str) -> "EconomyTripBuilder":
        """Set the name of the economy trip.

        Args:
            name: The name to set for the trip.

        Returns:
            Self for method chaining.
        """
        self.trip.name = name
        return self

    def set_destination(self, destination: str) -> "EconomyTripBuilder":
        """Set the destination of the economy trip.

        Args:
            destination: The destination to set for the trip.

        Returns:
            Self for method chaining.
        """
        self.trip.destination = destination
        return self

    def set_passengers(self, passengers: list[str]) -> "EconomyTripBuilder":
        """Set the passengers of the economy trip.

        Economy trips have no passenger limit, making them ideal for groups.

        Args:
            passengers: The list of passengers to set for the trip.

        Returns:
            Self for method chaining.
        """
        self.trip.passengers = passengers
        return self

    def set_budget(
        self,
        minimum_budget: float,
        maximum_budget: float,
    ) -> "EconomyTripBuilder":
        """Set the budget for the economy trip.

        Economy trips enforce a maximum budget cap per person to maintain
        affordability.

        Args:
            minimum_budget: The minimum budget for the trip.
            maximum_budget: The maximum budget for the trip.

        Returns:
            Self for method chaining.

        Raises:
            ValueError: If maximum budget is less than minimum budget or
                       exceeds the per-person cap.
        """
        if maximum_budget < minimum_budget:
            raise ValueError(
                "Maximum budget cannot be less than minimum budget",
            )

        # Enforce economy budget cap per person
        num_passengers = (
            len(self.trip.passengers) if self.trip.passengers else 1
        )
        max_allowed = self.MAX_BUDGET_PER_PERSON * num_passengers
        if maximum_budget > max_allowed:
            raise ValueError(
                f"Economy trip maximum budget cannot exceed "
                f"{self.MAX_BUDGET_PER_PERSON} per person "
                f"({max_allowed} for {num_passengers} passenger(s))",
            )

        self.trip.minimum_budget = minimum_budget
        self.trip.maximum_budget = maximum_budget
        return self

    def build(self) -> Trip:
        """Build and return the economy trip.

        Returns:
            The constructed economy Trip instance.
        """
        return self.trip


class LuxuryTripBuilder(TripBuilder):
    """Concrete builder for creating luxury trips.

    Luxury trips provide premium experiences with the following characteristics:
    - Minimum budget of 10,000 to ensure quality
    - Maximum of 4 passengers for exclusivity
    - Premium amenities included (5-star hotels, private transport, concierge)
    - Suitable for high-end travelers seeking personalized experiences
    """

    # Class constants for validation
    MIN_LUXURY_BUDGET = 10000.0
    MAX_PASSENGERS = 4
    DEFAULT_AMENITIES = [
        "5-star accommodation",
        "Private transport",
        "24/7 Concierge service",
        "Premium insurance",
    ]

    def __init__(self) -> None:
        """Initialize a new LuxuryTripBuilder with premium amenities."""
        self.trip = Trip(
            type=TripType.LUXURY,
            amenities=self.DEFAULT_AMENITIES.copy(),
        )

    def set_name(self, name: str) -> "LuxuryTripBuilder":
        """Set the name of the luxury trip.

        Args:
            name: The name to set for the trip.

        Returns:
            Self for method chaining.
        """
        self.trip.name = name
        return self

    def set_destination(self, destination: str) -> "LuxuryTripBuilder":
        """Set the destination of the luxury trip.

        Args:
            destination: The destination to set for the trip.

        Returns:
            Self for method chaining.
        """
        self.trip.destination = destination
        return self

    def set_passengers(self, passengers: list[str]) -> "LuxuryTripBuilder":
        """Set the passengers of the luxury trip.

        Luxury trips are limited to 4 passengers to maintain exclusivity
        and personalized service.

        Args:
            passengers: The list of passengers to set for the trip.

        Returns:
            Self for method chaining.

        Raises:
            ValueError: If passenger count exceeds maximum limit.
        """
        if len(passengers) > self.MAX_PASSENGERS:
            raise ValueError(
                f"Luxury trips are limited to {self.MAX_PASSENGERS} passengers "
                f"for exclusivity (got {len(passengers)})",
            )
        self.trip.passengers = passengers
        return self

    def set_budget(
        self,
        minimum_budget: float,
        maximum_budget: float,
    ) -> "LuxuryTripBuilder":
        """Set the budget for the luxury trip.

        Luxury trips enforce a minimum budget to ensure premium quality
        experiences and services.

        Args:
            minimum_budget: The minimum budget for the trip.
            maximum_budget: The maximum budget for the trip.

        Returns:
            Self for method chaining.

        Raises:
            ValueError: If budget is below luxury minimum or maximum is less
                       than minimum.
        """
        if maximum_budget < minimum_budget:
            raise ValueError(
                "Maximum budget cannot be less than minimum budget",
            )

        # Enforce luxury minimum budget
        if minimum_budget < self.MIN_LUXURY_BUDGET:
            raise ValueError(
                f"Luxury trips require a minimum budget of "
                f"{self.MIN_LUXURY_BUDGET} (got {minimum_budget})",
            )

        self.trip.minimum_budget = minimum_budget
        self.trip.maximum_budget = maximum_budget
        return self

    def build(self) -> Trip:
        """Build and return the luxury trip.

        Returns:
            The constructed luxury Trip instance.
        """
        return self.trip
