# Adapter pattern

<!-- markdownlint-disable MD046 -->
!!! info "Quality Score"
    **Overall Score**: 9.0/10 ⭐ Excellent

    - Technical Accuracy: 32/35
    - Code Quality: 25/25
    - Educational Value: 20/25
    - Documentation: 13/15

    Last reviewed: August 17, 2026
<!-- markdownlint-enable MD046 -->

The adapter pattern is a structural design pattern that allows object with
incompatible interfaces to work together, transforming the original interface
into a compatible interface. It is often used to make existing classes work with
others without modifying their source code. The benefits of this pattern are:

- **Reusability**: The adapter pattern allows for the reuse of existing classes,
  making it easier to integrate them into new systems.
- **Flexibility**: The adapter pattern allows for flexibility in the design of
  the system, allowing for the use of different classes with different
  interfaces.

The adapter pattern is composed of three main components:

## Target interface

The target interface represents the interface that the client expects. It
defines the methods that the adapter class must implement to be compatible with
the client.

::: src.advanced.adapter_pattern.AuthenticationInterface

## Adapter implementation

The adapter implementation is the class that implements the target interface and
adapts the existing class to the target interface. It has a reference to the
existing class and implements the methods of the target interface, transforming
the original interface into a compatible interface.

::: src.advanced.adapter_pattern.LoginAdapter

## Adaptee

The adaptee is the existing class that needs to be adapted to the target
interface, which has an incompatible interface.

::: src.advanced.adapter_pattern.Login

The real world applications of the adapter pattern are: supporting legacy
systems, reusing existing code that is hard to modify (complex or
closed-source), wrapping third-party libraries...
