# Facade pattern

<!-- markdownlint-disable MD046 -->
!!! info "Quality Score"
    **Overall Score**: 9.6/10 ⭐ Outstanding

    - Technical Accuracy: 34/35
    - Code Quality: 25/25
    - Educational Value: 23/25
    - Documentation: 14/15

    Last reviewed: August 15, 2026
<!-- markdownlint-enable MD046 -->

The facade pattern is a structural design pattern that provides a simplified
interface to a complex subsystem. It allows clients to interact with the
subsystem without needing to understand its internal workings. The benefits of
this pattern are:

- **Simplified interface**: The facade pattern provides an easy, simple and
  unified interface to a set of library or services, allowing quicker usage of
  the subsystem.
- **Decoupling**: The facade pattern decouples the client code from the complex
  subsystem, allowing for more flexible and maintainable code.
- **Single Responsibility Principle**: The facade pattern allows for the
  separation of concerns, allowing for a single responsibility for each class.
- **Encapsulation**: The facade pattern encapsulates the complexity of the
  subsystem, allowing for a more modular and maintainable codebase.

The facade pattern is composed of three main components:

## Facade

Defines the simplified interface to the complex subsystem. It should hide any
internal details, such as data model, connection to database, service calls,
etc.

::: src.advanced.facade_pattern.BookstoreFacade

## Subsystem

The subsystem is composed of multiple classes that work together to provide the
functionality of the subsystem. The subsystem classes should not be aware of the
facade, and should not depend on it. The subsystem classes should be designed to
work together, and should not be designed to work independently.

::: src.advanced.facade_pattern.BookManager
::: src.advanced.facade_pattern.InventoryBookStock
::: src.advanced.facade_pattern.IsbnValidator

## Client

The client is the code that uses the facade to interact with the subsystem. The
client should not be aware of the internal workings of the subsystem, and should
only interact with the facade. The client should be designed to work with the
facade, which is curated to expose only the necessary functionality, avoiding
using the complexity to init and manage the subsystem classes.

````python
store = BookstoreFacade.create()
store.new_book("9788413148465", "Project Hail Mary", "Andy Weir", 5)
store.purchase_book("9788413148465", 1)
```
Some good notes to keep in mind when using the facade pattern are:

- A big facade is a code smell. You can then split it into multiple smaller
  facades, each with a specific responsibility.
- Avoid exposing the subsystem classes to the client code. The facade should be
  the only point of contact for the client code. Create new data models to
  return from the facade, instead of returning the subsystem classes.
- to ensure that client code is using the facade, you can use a linter to
enforce that the subsystem classes are not used directly, such as
[import-linter](https://import-linter.readthedocs.io/en/stable/).


Some real-world examples are: complex libraries or frameworks, backend for
microservices, services that require multiple steps to perform a task, and
systems that require a simplified interface for end-users.
