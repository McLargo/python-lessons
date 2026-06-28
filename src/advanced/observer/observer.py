"""Observer pattern example in Python."""

import logging
from abc import ABC, abstractmethod

logging.basicConfig(format="%(message)s", level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Observer(ABC):
    """Abstract base class for observers."""

    @abstractmethod
    def update(self, message: str) -> None:
        """Receive an update from the subject.

        Args:
            message (str): The notification message from the subject.
        """
        pass


class KafkaObserver(Observer):
    """Concrete observer that simulates sending messages to Kafka."""

    def __init__(self, settings: dict) -> None:
        """Init the KafkaObserver with specific settings.

        Args:
            settings (dict): Configuration settings for the Kafka client.
        """
        self.settings = settings
        self._client = None  # Simulate a Kafka client

    def update(self, message: str) -> None:
        """Simulate sending a message to Kafka.

        Args:
            message (str): The message to send to Kafka.
        """
        logger.info("KafkaObserver received message: %s", message)


class RabbitMQObserver(Observer):
    """Concrete observer that simulates sending messages to RabbitMQ."""

    def __init__(self, settings: dict) -> None:
        """Init the RabbitMQObserver with specific settings.

        Args:
            settings (dict): Configuration settings for the RabbitMQ client.
        """
        self.settings = settings
        self._client = None  # Simulate a RabbitMQ client

    def update(self, message: str) -> None:
        """Simulate sending a message to RabbitMQ.

        Args:
            message (str): The message to send to RabbitMQ.
        """
        logger.info("RabbitMQObserver received message: %s", message)


class Subject:
    """Subject that maintains observers and notifies them of changes."""

    def __init__(self) -> None:
        """Initialize the subject with an empty list of observers."""
        self._observers: list[Observer] = []

    def subscribe(self, observer: Observer) -> None:
        """Add an observer to the subject.

        Args:
            observer (Observer): The observer to subscribe.
        """
        self._observers.append(observer)
        logger.info("Subscribed an observer: %s", observer.__class__.__name__)

    def unsubscribe(self, observer: Observer) -> None:
        """Remove an observer from the subject.

        Args:
            observer (Observer): The observer to unsubscribe.
        """
        self._observers.remove(observer)
        logger.info("Unsubscribed an observer: %s", observer.__class__.__name__)

    def notify(self, message: str) -> None:
        """Notify all subscribed observers with a message.

        Args:
            message (str): The message to send to all observers.
        """
        logger.info("Notifying observers...")
        for observer in self._observers:
            observer.update(message)
