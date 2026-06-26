# Strategy pattern

<!-- markdownlint-disable MD046 -->
!!! info "Quality Score"
    **Overall Score**: 8.8/10 ✅ Excellent

    - Technical Accuracy: 31/35
    - Code Quality: 23/25
    - Educational Value: 21/25
    - Documentation: 13/15

    Last reviewed: June 26, 2026
<!-- markdownlint-enable MD046 -->

The strategy pattern is a behavioral design pattern that defines a family of
algorithms, encapsulates each one, and makes them interchangeable. It lets the
algorithm vary independently from clients that use it, enabling selection at
runtime without modifying client code. The main use case to implement this pattern
is when you have multiple algorithms for a specific task and want to switch
between them at runtime. Main benefits of this pattern are:

- **Eliminates conditional logic**: Replace if/else chains with polymorphism
- **Encapsulation**: Each algorithm is self-contained and easier to test
- **Flexibility**: Add new strategies without modifying existing code
- **Runtime switching**: Change behavior dynamically based on context
- **Open/Closed Principle**: Open for extension, closed for modification

The strategy pattern is composed of three main components:

- **Strategy Interface**: Defines the common interface for all supported
  algorithms. The responsibility is to know how to execute, not when to use the
  strategy.

::: src.advanced.strategy_pattern.GreetingStrategy

- **Concrete Strategies**: Implement the specific algorithm to be used. Each
  concrete strategy encapsulates a different behavior.

::: src.advanced.strategy_pattern.EnglishGreeting
::: src.advanced.strategy_pattern.FrenchGreeting
::: src.advanced.strategy_pattern.SpanishGreeting

- **Context**: Maintains a reference to a Strategy object to use and delegates
  algorithm execution to it.

::: src.advanced.strategy_pattern.GreetingProcessor

Some real-world examples are: payment processing, data compression, export
formats, sorting algorithms, discount calculations...
