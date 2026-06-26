# Observer pattern

<!-- markdownlint-disable MD046 -->
!!! info "Quality Score"
    **Overall Score**: 8.6/10 ✅ Excellent

    - Technical Accuracy: 30/35
    - Code Quality: 24/25
    - Educational Value: 20/25
    - Documentation: 12/15

    Last reviewed: June 26, 2026
<!-- markdownlint-enable MD046 -->

The observer pattern is a behavioral design pattern used when you want to notify
multiple objects about a change of state/event in one object. The relationship
is one-to-many, so when the state of the subject changes, all its observers are
notified and updated automatically. The benefits of this pattern are:

- **Decoupling**: The subject and observers are loosely coupled, allowing for
  independent development and maintenance.
- **Dynamic relationships**: Observers can be added or removed at runtime,
  allowing for flexible and dynamic relationships between objects.
- **Broadcast communication**: The subject can notify multiple observers
  simultaneously, enabling efficient communication and reducing the need for
  direct dependencies between objects.
- **Event-driven architecture**: The observer pattern is commonly used in
  event-driven systems, where changes in one component trigger updates in other
  components.
- **Main use case**: When you need to notify different objects about changes in
  the state of another object.
- Avoid using the pattern when the relationship is one-to-one.

The observer pattern is composed of three main components:

- **Subject**: Maintains a list of observers and provides methods to attach,
  detach, and notify them. It is responsible for managing the state and
  notifying observers of any changes.

::: src.advanced.observer.Subject

- **Observer Interface**: Defines the update method that observers must
  implement to receive notifications from the subject. It establishes a contract
  for communication between the subject and observers.

::: src.advanced.observer.Observer

- **Concrete Observers**: Implement the observer interface and define the
  specific behavior to be executed when notified of a state change in the
  subject. Each concrete observer can have its own unique response to the
  notification.

::: src.advanced.observer.KafkaObserver
::: src.advanced.observer.RabbitMQObserver

Some real-world examples are: event-driven systems, notification systems,
pub-sub architectures, real-time data updates...
