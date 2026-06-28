"""Tests for the observer pattern implementation."""

from hypothesis import given
from hypothesis import strategies as st

from advanced.observer import (
    KafkaObserver,
    Observer,
    RabbitMQObserver,
    Subject,
)


class TestConcreteObservers:
    """Test each concrete observer individually."""

    def test_kafka_observer_update(self, caplog) -> None:
        """Test that KafkaObserver receives and logs messages correctly."""
        observer = KafkaObserver(settings={"broker": "localhost:9092"})
        observer.update("Test message")
        assert "KafkaObserver received message: Test message" in caplog.text

    def test_rabbitmq_observer_update(self, caplog) -> None:
        """Test that RabbitMQObserver receives and logs messages correctly."""
        observer = RabbitMQObserver(settings={"host": "localhost"})
        observer.update("Test message")
        assert "RabbitMQObserver received message: Test message" in caplog.text

    def test_observers_are_observer_instances(self) -> None:
        """Verify all observers implement the Observer interface."""
        kafka = KafkaObserver(settings={"broker": "localhost:9092"})
        rabbitmq = RabbitMQObserver(settings={"host": "localhost"})

        assert isinstance(kafka, Observer)
        assert isinstance(rabbitmq, Observer)

    def test_cannot_instantiate_abstract_observer(self) -> None:
        """Test that the abstract Observer class cannot be instantiated."""
        try:
            Observer()  # type: ignore
            assert False, "Should not be able to instantiate Observer"
        except TypeError as e:
            assert "abstract" in str(e).lower()
            assert "Observer" in str(e) or "update" in str(e)

    def test_kafka_observer_stores_settings(self) -> None:
        """Test that KafkaObserver stores settings correctly."""
        settings = {"broker": "localhost:9092", "topic": "events"}
        observer = KafkaObserver(settings=settings)
        assert observer.settings == settings

    def test_rabbitmq_observer_stores_settings(self) -> None:
        """Test that RabbitMQObserver stores settings correctly."""
        settings = {"host": "localhost", "queue": "messages"}
        observer = RabbitMQObserver(settings=settings)
        assert observer.settings == settings


class TestSubject:
    """Test the subject class behavior."""

    def test_subscribe_adds_observer(self, caplog) -> None:
        """Test that subscribe adds an observer to the subject."""
        subject = Subject()
        observer = KafkaObserver(settings={})

        subject.subscribe(observer)

        assert observer in subject._observers
        assert "Subscribed an observer: KafkaObserver" in caplog.text

    def test_subscribe_multiple_observers(self) -> None:
        """Test that multiple observers can be subscribed."""
        subject = Subject()
        kafka = KafkaObserver(settings={})
        rabbitmq = RabbitMQObserver(settings={})

        subject.subscribe(kafka)
        subject.subscribe(rabbitmq)

        assert len(subject._observers) == 2
        assert kafka in subject._observers
        assert rabbitmq in subject._observers

    def test_unsubscribe_removes_observer(self, caplog) -> None:
        """Test that unsubscribe removes an observer from the subject."""
        subject = Subject()
        observer = KafkaObserver(settings={})

        subject.subscribe(observer)
        subject.unsubscribe(observer)

        assert observer not in subject._observers
        assert "Unsubscribed an observer: KafkaObserver" in caplog.text

    def test_notify_sends_message_to_all_observers(self, caplog) -> None:
        """Test that notify sends messages to all subscribed observers."""
        subject = Subject()
        kafka = KafkaObserver(settings={})
        rabbitmq = RabbitMQObserver(settings={})

        subject.subscribe(kafka)
        subject.subscribe(rabbitmq)

        subject.notify("Test notification")

        assert "Notifying observers..." in caplog.text
        assert (
            "KafkaObserver received message: Test notification" in caplog.text
        )
        assert (
            "RabbitMQObserver received message: Test notification"
            in caplog.text
        )

    def test_notify_with_no_observers(self, caplog) -> None:
        """Test that notify works even when there are no observers."""
        subject = Subject()
        subject.notify("Test message")

        assert "Notifying observers..." in caplog.text

    def test_notify_after_unsubscribe(self, caplog) -> None:
        """Test that unsubscribed observers don't receive notifications."""
        subject = Subject()
        kafka = KafkaObserver(settings={})
        rabbitmq = RabbitMQObserver(settings={})

        subject.subscribe(kafka)
        subject.subscribe(rabbitmq)
        subject.unsubscribe(kafka)

        caplog.clear()
        subject.notify("Test message")

        assert "KafkaObserver received message" not in caplog.text
        assert "RabbitMQObserver received message: Test message" in caplog.text

    def test_subject_initializes_empty(self) -> None:
        """Test that a new Subject has no observers."""
        subject = Subject()
        assert len(subject._observers) == 0
        assert subject._observers == []


class TestObserverPropertyBased:
    """Property-based tests using Hypothesis."""

    @given(message=st.text(min_size=0, max_size=1000))
    def test_observers_handle_any_message(self, message: str) -> None:
        """Property: Observers should handle any message string."""
        kafka = KafkaObserver(settings={})
        rabbitmq = RabbitMQObserver(settings={})

        # Should not raise any exception
        kafka.update(message)
        rabbitmq.update(message)

    @given(
        message=st.text(min_size=1, max_size=500),
        settings=st.dictionaries(
            keys=st.text(min_size=1, max_size=50),
            values=st.one_of(
                st.text(min_size=0, max_size=100),
                st.integers(),
                st.booleans(),
            ),
            min_size=0,
            max_size=10,
        ),
    )
    def test_observers_accept_any_valid_settings(
        self,
        message: str,
        settings: dict,
    ) -> None:
        """Property: Observers work with any valid settings dictionary."""
        kafka = KafkaObserver(settings=settings)
        rabbitmq = RabbitMQObserver(settings=settings)

        assert kafka.settings == settings
        assert rabbitmq.settings == settings

        # Should handle messages with any settings
        kafka.update(message)
        rabbitmq.update(message)

    @given(
        message=st.text(min_size=0, max_size=500),
        num_observers=st.integers(min_value=1, max_value=10),
    )
    def test_all_observers_receive_same_message(
        self,
        message: str,
        num_observers: int,
    ) -> None:
        """Property: All subscribed observers receive notifications."""
        subject = Subject()
        observers = [KafkaObserver(settings={}) for _ in range(num_observers)]

        for observer in observers:
            subject.subscribe(observer)

        # Should not raise any exception
        subject.notify(message)

        # All observers should still be subscribed
        assert len(subject._observers) == num_observers

    @given(num_subscribe=st.integers(min_value=0, max_value=20))
    def test_subscribe_unsubscribe_consistency(
        self,
        num_subscribe: int,
    ) -> None:
        """Property: Subscribe/unsubscribe maintains consistency."""
        subject = Subject()
        observers = [KafkaObserver(settings={}) for _ in range(num_subscribe)]

        # Subscribe all
        for observer in observers:
            subject.subscribe(observer)

        assert len(subject._observers) == num_subscribe

        # Unsubscribe all
        for observer in observers:
            subject.unsubscribe(observer)

        assert len(subject._observers) == 0

    @given(
        messages=st.lists(
            st.text(min_size=1, max_size=100),
            min_size=1,
            max_size=10,
        ),
    )
    def test_multiple_notifications(
        self,
        messages: list[str],
    ) -> None:
        """Property: Multiple notifications work without errors."""
        subject = Subject()
        observer = KafkaObserver(settings={})
        subject.subscribe(observer)

        # Should handle multiple notifications without errors
        for message in messages:
            subject.notify(message)

        # Observer should still be subscribed
        assert observer in subject._observers

    @given(
        message=st.text(min_size=1, max_size=200),
        num_kafka=st.integers(min_value=0, max_value=5),
        num_rabbitmq=st.integers(min_value=0, max_value=5),
    )
    def test_mixed_observer_types(
        self,
        message: str,
        num_kafka: int,
        num_rabbitmq: int,
    ) -> None:
        """Property: Mixed observer types all get subscribed correctly."""
        subject = Subject()

        kafka_observers = [KafkaObserver(settings={}) for _ in range(num_kafka)]
        rabbitmq_observers = [
            RabbitMQObserver(settings={}) for _ in range(num_rabbitmq)
        ]

        for observer in kafka_observers + rabbitmq_observers:
            subject.subscribe(observer)

        total_observers = num_kafka + num_rabbitmq
        assert len(subject._observers) == total_observers

        # Should notify without errors
        subject.notify(message)

        # All observers should still be subscribed
        for observer in kafka_observers:
            assert observer in subject._observers
        for observer in rabbitmq_observers:
            assert observer in subject._observers
