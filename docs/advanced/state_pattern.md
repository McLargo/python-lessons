# State pattern

<!-- markdownlint-disable MD046 -->
!!! info "Quality Score"
    **Overall Score**: 9.3/10 ⭐ Excellent

    - Technical Accuracy: 33/35
    - Code Quality: 25/25
    - Educational Value: 21/25
    - Documentation: 14/15

    Last reviewed: July 2, 2026
<!-- markdownlint-enable MD046 -->

State pattern is a behavioral design pattern that allows an object to change its
default behavior when its internal state changes. Once the state of an object
is updated, the object will react differently to the same input. It is very
useful when you expect an object to react differently based on its state.

The simple use case of state pattern is a state machine. A state machine is an
algorithm that represents a set of states and the transitions between those
states. Then, state machine can be used to model the behavior of an object that
can be in different states. For example, a user can be in different states like
pending, active, inactive and closed. Once the user changes from one state to
another, the user can or cannot perform different actions (like login is only
allowed when the user is active).

The main benefits of this pattern are:

- **Encapsulation**: Each state is self-contained and easier to test
- **Flexibility**: Add new states without modifying existing code
- **Maintainability**: Each state is a separate class, making it easier to
  maintain and understand the code

The state pattern is composed of three main components:

## State Interface

Defines the common interface for all supported states. The responsibility is to
know how to execute, not when to use the state. The interface is usually
implemented as an abstract class.

::: src.advanced.state_pattern.UserState

## Concrete State

Implements the behavior associated with a state of the context. The
responsibility is to know how to execute and where state to transition, not when
to use the state.

::: src.advanced.state_pattern.Pending

::: src.advanced.state_pattern.Active

::: src.advanced.state_pattern.Inactive

::: src.advanced.state_pattern.Closed

## Context

Maintains an instance of the class that defines the current state. The
responsibility is to know when to use the state, not how to execute it.

::: src.advanced.state_pattern.User

Some real world applications of the state pattern are: orders and e-shopping
carts, workflows, finance, media streaming... everything that can be modeled as
a state machine can benefit from the state pattern.
