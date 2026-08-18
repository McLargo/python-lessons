# Bridge pattern

<!-- markdownlint-disable MD046 -->
!!! info "Quality Score"
    **Overall Score**: 9.4/10 ⭐ Outstanding

    - Technical Accuracy: 32/35
    - Code Quality: 25/25
    - Educational Value: 24/25
    - Documentation: 13/15

    Last reviewed: August 18, 2026
<!-- markdownlint-enable MD046 -->

The bridge pattern is a structural design pattern that decouples an abstraction
from its implementation, allowing the two to vary independently. It is useful
when you want to avoid a permanent binding between an abstraction and its
implementation, enabling flexibility and scalability in your code. The benefits
are:

- **Decoupling**: The bridge pattern separates the abstraction from its
  implementation, allowing them to evolve independently. This makes it easier to
  modify or extend either the abstraction or the implementation without
  affecting the other.
- **Flexibility**: By using the bridge pattern, you can easily switch between
  different implementations of an abstraction at runtime. This is particularly
  useful when you have multiple variations of an abstraction that need to be
  combined with different implementations.
- **Scalability**: The bridge pattern promotes scalability by allowing you to
  add new abstractions and implementations independently, without affecting
  existing code. This makes it easier to grow and maintain your system over
  time.

The beauty of the bridge pattern is that it is inherent in Python, making it
easy to implement. It has two main components

## Abstraction

The interface that defines the abstraction and maintains a reference to an
object of the implementation hierarchy. The abstraction can be an abstract class
or an interface that defines the common behavior for the abstraction, even can
be extended without modifying the implementation.

::: src.advanced.bridge_pattern.Mode
::: src.advanced.bridge_pattern.Element

## Implementation

Implementation defines the interface for the implementation classes. It is
responsible for providing the concrete implementation of the abstraction's
behavior. New implementations can be added without changing the abstraction and
without much effort. Also, implementations can be extended independently without
affecting the others.

::: src.advanced.bridge_pattern.LightMode
::: src.advanced.bridge_pattern.DarkMode
::: src.advanced.bridge_pattern.ColorBlindMode

::: src.advanced.bridge_pattern.Navbar
::: src.advanced.bridge_pattern.Footer

The common usage of the bridge pattern is often used in GUI frameworks, where
you have different types of UI elements (abstractions) that can be rendered
using different rendering engines (implementations).
