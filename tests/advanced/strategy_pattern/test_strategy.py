"""Tests for the strategy pattern implementation."""

import pytest
from hypothesis import given
from hypothesis import strategies as st

from advanced.strategy_pattern import (
    EnglishGreeting,
    FrenchGreeting,
    GreetingProcessor,
    GreetingStrategy,
    SpanishGreeting,
)


@given(
    name=st.one_of(
        st.text(min_size=1, max_size=1),
        st.text(min_size=100, max_size=1000),
        st.text(
            alphabet=st.characters(
                blacklist_categories=("Cs",),
                min_codepoint=0x0020,
            ),
            min_size=1,
        ),
        st.just(" " * 10),
        st.text(alphabet="123456789", min_size=1),
        st.just(""),
    ),
)
def test_strategies_handle_edge_case_names(name: str) -> None:
    """Property: Strategies should handle all valid string edge cases."""
    strategies = [
        SpanishGreeting(),
        FrenchGreeting(),
        EnglishGreeting(),
    ]

    for strategy in strategies:
        result = strategy.greet(name)

        assert isinstance(result, str)
        assert name in result
        assert len(result) > len(name)


class TestConcreteStrategies:
    """Test each concrete strategy individually."""

    def test_spanish_greeting(self) -> None:
        strategy = SpanishGreeting()
        result = strategy.greet("Alice")
        assert result == "Hola, Alice!"

    def test_french_greeting(self) -> None:
        strategy = FrenchGreeting()
        result = strategy.greet("Bob")
        assert result == "Bonjour, Bob!"

    def test_english_greeting(self) -> None:
        strategy = EnglishGreeting()
        result = strategy.greet("Charlie")
        assert result == "Hello, Charlie!"

    def test_strategies_are_greeting_strategy_instances(self) -> None:
        """Verify all strategies implement the GreetingStrategy interface."""
        spanish = SpanishGreeting()
        french = FrenchGreeting()
        english = EnglishGreeting()

        assert isinstance(spanish, GreetingStrategy)
        assert isinstance(french, GreetingStrategy)
        assert isinstance(english, GreetingStrategy)


class TestGreetingProcessor:
    """Test the context class behavior."""

    def test_processor_with_spanish_strategy(self) -> None:
        processor = GreetingProcessor(SpanishGreeting())
        result = processor.process_greeting("Maria")
        assert result == "Hola, Maria!"

    def test_processor_with_french_strategy(self) -> None:
        processor = GreetingProcessor(FrenchGreeting())
        result = processor.process_greeting("Pierre")
        assert result == "Bonjour, Pierre!"

    def test_processor_with_english_strategy(self) -> None:
        processor = GreetingProcessor(EnglishGreeting())
        result = processor.process_greeting("John")
        assert result == "Hello, John!"


class TestRuntimeStrategySwitching:
    """Test the key benefit: changing strategies at runtime."""

    def test_switch_from_spanish_to_french(self) -> None:
        processor = GreetingProcessor(SpanishGreeting())

        # Initial strategy
        result1 = processor.process_greeting("Alex")
        assert result1 == "Hola, Alex!"

        # Switch strategy at runtime
        processor.set_strategy(FrenchGreeting())
        result2 = processor.process_greeting("Alex")
        assert result2 == "Bonjour, Alex!"

    def test_switch_multiple_strategies(self) -> None:
        """Test switching between multiple strategies on same processor."""
        processor = GreetingProcessor(SpanishGreeting())
        name = "Sam"

        # Spanish
        assert processor.process_greeting(name) == "Hola, Sam!"

        # Switch to French
        processor.set_strategy(FrenchGreeting())
        assert processor.process_greeting(name) == "Bonjour, Sam!"

        # Switch to English
        processor.set_strategy(EnglishGreeting())
        assert processor.process_greeting(name) == "Hello, Sam!"

        # Switch back to Spanish
        processor.set_strategy(SpanishGreeting())
        assert processor.process_greeting(name) == "Hola, Sam!"

    def test_same_name_different_strategies(self) -> None:
        """Verify same input gives different output per strategy."""
        name = "Taylor"

        spanish_processor = GreetingProcessor(SpanishGreeting())
        french_processor = GreetingProcessor(FrenchGreeting())
        english_processor = GreetingProcessor(EnglishGreeting())

        spanish_result = spanish_processor.process_greeting(name)
        french_result = french_processor.process_greeting(name)
        english_result = english_processor.process_greeting(name)

        # All results should be different
        assert spanish_result == "Hola, Taylor!"
        assert french_result == "Bonjour, Taylor!"
        assert english_result == "Hello, Taylor!"
        assert spanish_result != french_result != english_result


class TestStrategyInterchangeability:
    """Test that strategies are truly interchangeable."""

    @pytest.mark.parametrize(
        "strategy_class,expected_greeting",
        [
            (SpanishGreeting, "Hola, Test!"),
            (FrenchGreeting, "Bonjour, Test!"),
            (EnglishGreeting, "Hello, Test!"),
        ],
    )
    def test_all_strategies_work_with_processor(
        self,
        strategy_class,
        expected_greeting,
    ) -> None:
        """Verify any strategy can be used with the processor."""
        strategy = strategy_class()
        processor = GreetingProcessor(strategy)
        result = processor.process_greeting("Test")
        assert result == expected_greeting

    def test_processor_accepts_any_greeting_strategy(self) -> None:
        """Verify processor accepts any GreetingStrategy implementation."""
        strategies = [
            SpanishGreeting(),
            FrenchGreeting(),
            EnglishGreeting(),
        ]

        for strategy in strategies:
            # Should not raise any exception
            processor = GreetingProcessor(strategy)
            assert processor._strategy == strategy
