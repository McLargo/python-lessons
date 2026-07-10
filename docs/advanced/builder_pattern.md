# Builder pattern

<!-- markdownlint-disable MD046 -->
!!! info "Quality Score"
    **Overall Score**: 9.5/10 ⭐ Outstanding

    - Technical Accuracy: 33/35
    - Code Quality: 25/25
    - Educational Value: 23/25
    - Documentation: 14/15
<!-- markdownlint-enable MD046 -->

The builder pattern is a creational pattern that allows to create complex
object step-by-step. The default constructor of the object is not used, instead
a builder class is used to make new instances of the object. The builder class
has methods to set the properties of the object, returning the object itself at
the end of each method. Using this pattern, you can construct different
representations of the same object. Builder also validates the different
properties if the object, ensuring that object is always in a valid state. The
main benefits of this pattern are:

- **Encapsulation**: The builder pattern encapsulates the construction of an
  object, allowing for more flexible and maintainable code.
- **Validation**: The builder pattern allows for validation of the object's
  properties, ensuring that the object is always in a valid state.
- **Fluent Interface**: The builder pattern allows for a fluent interface,
  making the code more readable and expressive.

The builder pattern is composed of three main components:

## Builder interface

The builder interface represents a abstract class that define the methods that
the concrete builder class must implement. It defines the methods to set the
properties of the object, returning the object itself at the end of each method.

::: src.advanced.builder_pattern.TripBuilder

The builder interface is not strictly necessary, but it is a good practice to
define an interface for the builder, allowing for more flexibility and
maintainability.

## Builder implementation

The builder implementation is responsible for constructing the object, applying
business logic. It has implemented the methods to set the properties of the
object, returning the object itself at the end of each method.
Also, it has a method to return the constructed object.

::: src.advanced.builder_pattern.EconomyTripBuilder

::: src.advanced.builder_pattern.LuxuryTripBuilder

## Entity

The entity represents the object that is being constructed. It has all the
properties that can be set by the builder, and it is responsible for maintaining
the state of the object. No business logic is applied in the entity, it is only
a data structure. Only consider to introduce any business logic when it is
clearly related to the state of the object, and not to the construction process.

::: src.advanced.builder_pattern.Trip

Some real world applications of the builder pattern are: complex object creation
and multiple object constructions.

## Common pitfalls

A common pitfall of the builder pattern is to introduce business logic in the
entity, instead of the builder. The entity should only be a data structure, and
the builder should be responsible for applying business logic to construct the
object.

Another common pitfall is to not validate the properties of the object
in the builder, allowing for the object to be in an invalid state. The builder
should always validate the properties before constructing the object.
