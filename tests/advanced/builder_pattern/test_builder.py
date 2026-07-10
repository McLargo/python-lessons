"""Tests for the builder pattern implementation."""

import pytest

from advanced.builder_pattern import (
    EconomyTripBuilder,
    LuxuryTripBuilder,
    Trip,
    TripType,
)


class TestTrip:
    """Test cases for the Trip dataclass."""

    def test_trip_initialization_defaults(self) -> None:
        """Test that Trip initializes with correct default values."""
        trip = Trip()
        assert trip.name == ""
        assert trip.destination == ""
        assert trip.passengers == []
        assert trip.minimum_budget == 0.0
        assert trip.maximum_budget == 0.0
        assert trip.type == TripType.ECONOMY
        assert trip.amenities == []

    def test_trip_initialization_with_values(self) -> None:
        """Test that Trip initializes correctly with provided values."""
        passengers = ["Alice", "Bob"]
        amenities = ["WiFi", "Breakfast"]

        trip = Trip(
            name="Summer Vacation",
            destination="Paris",
            passengers=passengers,
            minimum_budget=1000.0,
            maximum_budget=2000.0,
            type=TripType.LUXURY,
            amenities=amenities,
        )

        assert trip.name == "Summer Vacation"
        assert trip.destination == "Paris"
        assert trip.passengers == passengers
        assert trip.minimum_budget == 1000.0
        assert trip.maximum_budget == 2000.0
        assert trip.type == TripType.LUXURY
        assert trip.amenities == amenities

    def test_trip_string_representation(self) -> None:
        """Test that Trip __str__ method returns correct format."""
        trip = Trip(
            name="Beach Trip",
            destination="Cancun",
            passengers=["Alice"],
            minimum_budget=1000.0,
            maximum_budget=2000.0,
            type=TripType.ECONOMY,
            amenities=["Pool", "Beach access"],
        )

        result = str(trip)
        assert "Economy trip" in result
        assert "Beach Trip" in result
        assert "Cancun" in result
        assert "1" in result  # passenger count
        assert "1000" in result  # budget
        assert "Pool, Beach access" in result

    def test_trip_string_representation_no_amenities(self) -> None:
        """Test Trip string representation when no amenities."""
        trip = Trip(
            name="Simple Trip",
            destination="Local",
            type=TripType.ECONOMY,
        )
        result = str(trip)
        assert "amenities: -" in result


class TestEconomyTripBuilder:
    """Test cases for the EconomyTripBuilder."""

    def test_initialization(self) -> None:
        """Test that EconomyTripBuilder initializes correctly."""
        builder = EconomyTripBuilder()
        assert builder.trip.type == TripType.ECONOMY
        assert "Standard accommodation" in builder.trip.amenities
        assert "Group transport" in builder.trip.amenities

    def test_set_name_returns_builder(self) -> None:
        """Test that set_name returns self for chaining."""
        builder = EconomyTripBuilder()
        result = builder.set_name("Budget Adventure")
        assert result is builder
        assert builder.trip.name == "Budget Adventure"

    def test_set_destination_returns_builder(self) -> None:
        """Test that set_destination returns self for chaining."""
        builder = EconomyTripBuilder()
        result = builder.set_destination("Barcelona")
        assert result is builder
        assert builder.trip.destination == "Barcelona"

    def test_set_passengers_returns_builder(self) -> None:
        """Test that set_passengers returns self for chaining."""
        builder = EconomyTripBuilder()
        passengers = ["Alice", "Bob", "Charlie"]
        result = builder.set_passengers(passengers)
        assert result is builder
        assert builder.trip.passengers == passengers

    def test_set_passengers_allows_large_groups(self) -> None:
        """Test that economy trips allow large groups (no limit)."""
        builder = EconomyTripBuilder()
        passengers = [f"Person{i}" for i in range(20)]
        builder.set_passengers(passengers)
        assert len(builder.trip.passengers) == 20

    def test_set_budget_returns_builder(self) -> None:
        """Test that set_budget returns self for chaining."""
        builder = EconomyTripBuilder()
        builder.set_passengers(["Alice", "Bob"])
        result = builder.set_budget(500.0, 2000.0)
        assert result is builder
        assert builder.trip.minimum_budget == 500.0
        assert builder.trip.maximum_budget == 2000.0

    def test_set_budget_enforces_per_person_cap(self) -> None:
        """Test that economy builder enforces 1000 per person cap."""
        builder = EconomyTripBuilder()
        builder.set_passengers(["Alice", "Bob"])  # 2 passengers

        # 2,000 total = 1000 per person, should be OK
        builder.set_budget(500.0, 2000.0)
        assert builder.trip.maximum_budget == 2000.0

        # 2,001 exceeds cap
        with pytest.raises(ValueError, match="cannot exceed.*per person"):
            builder.set_budget(500.0, 2001.0)

    def test_set_budget_cap_with_single_passenger(self) -> None:
        """Test budget cap works correctly with single passenger."""
        builder = EconomyTripBuilder()
        builder.set_passengers(["Alice"])

        # Max 1000 for 1 passenger
        builder.set_budget(300.0, 1000.0)
        assert builder.trip.maximum_budget == 1000.0

        with pytest.raises(ValueError, match="cannot exceed"):
            builder.set_budget(300.0, 1001.0)

    def test_set_budget_cap_with_no_passengers_defaults_to_one(self) -> None:
        """Test budget cap assumes 1 passenger if none set."""
        builder = EconomyTripBuilder()
        # No passengers set, should default to 1

        builder.set_budget(300.0, 1000.0)
        assert builder.trip.maximum_budget == 1000.0

        with pytest.raises(ValueError, match="cannot exceed"):
            builder.set_budget(300.0, 1001.0)

    def test_set_budget_raises_error_if_max_less_than_min(self) -> None:
        """Test that set_budget raises error if max < min."""
        builder = EconomyTripBuilder()
        builder.set_passengers(["Alice"])

        with pytest.raises(
            ValueError,
            match="Maximum budget cannot be less than minimum budget",
        ):
            builder.set_budget(800.0, 500.0)

    def test_build_returns_trip(self) -> None:
        """Test that build() returns the constructed Trip."""
        builder = EconomyTripBuilder()
        trip = builder.build()
        assert isinstance(trip, Trip)
        assert trip.type == TripType.ECONOMY

    def test_method_chaining(self) -> None:
        """Test that all methods support fluent interface chaining."""
        builder = EconomyTripBuilder()

        trip = (
            builder.set_name("Budget Europe Tour")
            .set_destination("Multiple cities")
            .set_passengers(["Alice", "Bob", "Charlie"])
            .set_budget(300.0, 900.0)
            .build()
        )

        assert trip.name == "Budget Europe Tour"
        assert trip.destination == "Multiple cities"
        assert len(trip.passengers) == 3
        assert trip.minimum_budget == 300.0
        assert trip.maximum_budget == 900.0
        assert trip.type == TripType.ECONOMY

    def test_amenities_are_copied_not_shared(self) -> None:
        """Test that each builder instance has its own amenities list."""
        builder1 = EconomyTripBuilder()
        builder2 = EconomyTripBuilder()

        builder1.trip.amenities.append("Extra service")

        assert "Extra service" in builder1.trip.amenities
        assert "Extra service" not in builder2.trip.amenities


class TestLuxuryTripBuilder:
    """Test cases for the LuxuryTripBuilder."""

    def test_initialization(self) -> None:
        """Test that LuxuryTripBuilder initializes correctly."""
        builder = LuxuryTripBuilder()
        assert builder.trip.type == TripType.LUXURY
        assert "5-star accommodation" in builder.trip.amenities
        assert "Private transport" in builder.trip.amenities
        assert "24/7 Concierge service" in builder.trip.amenities
        assert "Premium insurance" in builder.trip.amenities

    def test_set_name_returns_builder(self) -> None:
        """Test that set_name returns self for chaining."""
        builder = LuxuryTripBuilder()
        result = builder.set_name("Exclusive Retreat")
        assert result is builder
        assert builder.trip.name == "Exclusive Retreat"

    def test_set_destination_returns_builder(self) -> None:
        """Test that set_destination returns self for chaining."""
        builder = LuxuryTripBuilder()
        result = builder.set_destination("Maldives")
        assert result is builder
        assert builder.trip.destination == "Maldives"

    def test_set_passengers_returns_builder(self) -> None:
        """Test that set_passengers returns self for chaining."""
        builder = LuxuryTripBuilder()
        passengers = ["VIP1", "VIP2"]
        result = builder.set_passengers(passengers)
        assert result is builder
        assert builder.trip.passengers == passengers

    def test_set_passengers_enforces_4_passenger_limit(self) -> None:
        """Test that luxury trips are limited to 4 passengers."""
        builder = LuxuryTripBuilder()

        # 4 passengers should be OK
        builder.set_passengers(["A", "B", "C", "D"])
        assert len(builder.trip.passengers) == 4

        # 5 passengers should fail
        with pytest.raises(ValueError, match="limited to 4 passengers"):
            builder.set_passengers(["A", "B", "C", "D", "E"])

    def test_set_passengers_allows_fewer_than_max(self) -> None:
        """Test that luxury trips allow fewer than max passengers."""
        builder = LuxuryTripBuilder()
        builder.set_passengers(["Alice"])
        assert len(builder.trip.passengers) == 1

    def test_set_budget_returns_builder(self) -> None:
        """Test that set_budget returns self for chaining."""
        builder = LuxuryTripBuilder()
        result = builder.set_budget(15000.0, 25000.0)
        assert result is builder
        assert builder.trip.minimum_budget == 15000.0
        assert builder.trip.maximum_budget == 25000.0

    def test_set_budget_enforces_minimum_luxury_budget(self) -> None:
        """Test that luxury builder enforces 10,000 minimum."""
        builder = LuxuryTripBuilder()

        # 10,000 minimum should be OK
        builder.set_budget(10000.0, 15000.0)
        assert builder.trip.minimum_budget == 10000.0

        # Below 10,000 should fail
        with pytest.raises(ValueError, match="minimum budget of.*10000"):
            builder.set_budget(9999.0, 15000.0)

    def test_set_budget_raises_error_if_max_less_than_min(self) -> None:
        """Test that set_budget raises error if max < min."""
        builder = LuxuryTripBuilder()

        with pytest.raises(
            ValueError,
            match="Maximum budget cannot be less than minimum budget",
        ):
            builder.set_budget(20000.0, 15000.0)

    def test_set_budget_allows_high_budgets(self) -> None:
        """Test that luxury trips can have very high budgets."""
        builder = LuxuryTripBuilder()
        builder.set_budget(50000.0, 100000.0)
        assert builder.trip.maximum_budget == 100000.0

    def test_build_returns_trip(self) -> None:
        """Test that build() returns the constructed Trip."""
        builder = LuxuryTripBuilder()
        trip = builder.build()
        assert isinstance(trip, Trip)
        assert trip.type == TripType.LUXURY

    def test_method_chaining(self) -> None:
        """Test that all methods support fluent interface chaining."""
        builder = LuxuryTripBuilder()

        trip = (
            builder.set_name("Monaco Grand Prix Experience")
            .set_destination("Monaco")
            .set_passengers(["VIP1", "VIP2"])
            .set_budget(25000.0, 50000.0)
            .build()
        )

        assert trip.name == "Monaco Grand Prix Experience"
        assert trip.destination == "Monaco"
        assert len(trip.passengers) == 2
        assert trip.minimum_budget == 25000.0
        assert trip.maximum_budget == 50000.0
        assert trip.type == TripType.LUXURY

    def test_amenities_are_copied_not_shared(self) -> None:
        """Test that each builder instance has its own amenities list."""
        builder1 = LuxuryTripBuilder()
        builder2 = LuxuryTripBuilder()

        builder1.trip.amenities.append("Helicopter transfer")

        assert "Helicopter transfer" in builder1.trip.amenities
        assert "Helicopter transfer" not in builder2.trip.amenities


class TestBuilderPatternIntegration:
    """Integration tests comparing Economy and Luxury builders."""

    def test_economy_vs_luxury_amenities(self) -> None:
        """Test that economy and luxury trips have different amenities."""
        economy = EconomyTripBuilder().build()
        luxury = LuxuryTripBuilder().build()

        assert len(economy.amenities) < len(luxury.amenities)
        assert "5-star accommodation" not in economy.amenities
        assert "5-star accommodation" in luxury.amenities

    def test_economy_vs_luxury_passenger_limits(self) -> None:
        """Test different passenger limit enforcement."""
        # Economy: large group OK
        economy = EconomyTripBuilder()
        economy.set_passengers([f"P{i}" for i in range(10)])
        assert len(economy.trip.passengers) == 10

        # Luxury: large group fails
        luxury = LuxuryTripBuilder()
        with pytest.raises(ValueError, match="limited to 4 passengers"):
            luxury.set_passengers([f"P{i}" for i in range(10)])

    def test_economy_vs_luxury_budget_constraints(self) -> None:
        """Test different budget constraints for each builder."""
        # Economy: low budgets OK, but capped per person
        economy = EconomyTripBuilder()
        economy.set_passengers(["Alice"])
        economy.set_budget(500.0, 1000.0)
        assert economy.trip.minimum_budget == 500.0

        # Luxury: low budgets fail
        luxury = LuxuryTripBuilder()
        with pytest.raises(ValueError, match="minimum budget"):
            luxury.set_budget(500.0, 3000.0)

    def test_polymorphism_with_builder_interface(self) -> None:
        """Test that both builders can be used polymorphically."""

        def create_trip_with_builder(
            builder: EconomyTripBuilder | LuxuryTripBuilder,
        ) -> Trip:
            """Helper function demonstrating polymorphic usage."""
            return (
                builder.set_name("Generic Trip")
                .set_destination("Somewhere")
                .build()
            )

        economy_trip = create_trip_with_builder(EconomyTripBuilder())
        luxury_trip = create_trip_with_builder(LuxuryTripBuilder())

        assert economy_trip.type == TripType.ECONOMY
        assert luxury_trip.type == TripType.LUXURY
        assert economy_trip.name == luxury_trip.name == "Generic Trip"


class TestTripType:
    """Test cases for TripType constants."""

    def test_trip_type_constants(self) -> None:
        """Test that TripType has the correct constant values."""
        assert TripType.ECONOMY == "Economy"
        assert TripType.LUXURY == "Luxury"

    def test_trip_type_only_has_two_types(self) -> None:
        """Test that TripType only defines Economy and Luxury."""
        trip_types = [
            attr
            for attr in dir(TripType)
            if not attr.startswith("_") and attr.isupper()
        ]
        assert set(trip_types) == {"ECONOMY", "LUXURY"}
