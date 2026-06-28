"""Strategy pattern example in Python."""

from abc import ABC, abstractmethod


class GreetingStrategy(ABC):
    """Abstract base class for greeting strategies."""

    @abstractmethod
    def greet(self, name: str) -> str:
        """Return a greeting message for the given name.

        Args:
            name (str): The name of the person to greet.

        Returns:
            str: A greeting message.
        """
        pass


class SpanishGreeting(GreetingStrategy):
    """Concrete strategy for Spanish greeting."""

    def greet(self, name: str) -> str:
        """Return a greeting message in Spanish for the given name.

        Args:
            name (str): The name of the person to greet.

        Returns:
            str: A greeting message in Spanish.
        """
        return f"Hola, {name}!"


class FrenchGreeting(GreetingStrategy):
    """Concrete strategy for French greeting."""

    def greet(self, name: str) -> str:
        """Return a greeting message in French for the given name.

        Args:
            name (str): The name of the person to greet.

        Returns:
            str: A greeting message in French.
        """
        return f"Bonjour, {name}!"


class EnglishGreeting(GreetingStrategy):
    """Concrete strategy for English greeting."""

    def greet(self, name: str) -> str:
        """Return a greeting message in English for the given name.

        Args:
            name (str): The name of the person to greet.

        Returns:
            str: A greeting message in English.
        """
        return f"Hello, {name}!"


class GreetingProcessor:
    """Context class that uses a greeting strategy given a person."""

    def __init__(self, strategy: GreetingStrategy) -> None:
        """Init the GreetingProcessor with a specific greeting strategy.

        Args:
            strategy (GreetingStrategy): The initial greeting strategy to use.
        """
        self._strategy = strategy

    def set_strategy(self, strategy: GreetingStrategy) -> None:
        """Set the greeting strategy.

        Args:
            strategy (GreetingStrategy): The new greeting strategy to use.
        """
        self._strategy = strategy

    def process_greeting(self, name: str) -> str:
        """Greet the person using the current strategy.

        Args:
            name (str): The name of the person to greet.

        Returns:
            str: A greeting message using the current strategy.
        """
        return self._strategy.greet(name)
