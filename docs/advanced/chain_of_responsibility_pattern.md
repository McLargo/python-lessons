# Chain of Responsibility Pattern

<!-- markdownlint-disable MD046 -->
!!! info "Quality Score"
    **Overall Score**: 9.4/10 ⭐ Outstanding

    - Technical Accuracy: 33/35
    - Code Quality: 25/25
    - Educational Value: 23/25
    - Documentation: 14/15

    Last reviewed: July 7, 2026
<!-- markdownlint-enable MD046 -->

Chain of responsibility is a behavioral design pattern that allows passing
request along a series of handlers. When receiving a request, each handler
decides to handle it with its own logic and/or pass it to the next handler in the
chain. Once the last handler is reached, the request is completed.

Each handler in the chain has a reference to the next handler, allowing for the
request to keep moving along the chain to the end. At any point, the request can
be handled and passed to the next handler, or it can be handled and the chain
can be terminated. You can use the Chain of Responsibility pattern when multiple
objects can handle a request, but the handler isn't known in advance or when you
need to process a request through multiple stages or validations. The main
benefits of this pattern are:

- **Decoupling**: The sender of a request is decoupled from the receiver,
  allowing for more flexible and maintainable code.
- **Dynamic Handling**: Handlers can be added or removed at runtime, allowing
  for dynamic handling of requests.
- **Responsibility Sharing**: Multiple handlers can share the responsibility of
  handling a request, allowing for more complex processing.
- **User journey**: The pattern can be used to create a user journey where each
  handler represents a step in the process, making a clear and organized flow of
  actions.

The chain of responsibility pattern is composed of three main components:

## Handler Interface

Defines the common interface for all supported
  handlers. The responsibility is to know how to handle a request, not when to
  use the handler. The interface is usually implemented as an abstract class.

::: src.advanced.chain_of_responsibility_pattern.Handler

## Concrete Handler

Implements the behavior associated with a handler of the chain. The
responsibility is to know how to handle a request and where to pass it next, not
when to use the handler.

::: src.advanced.chain_of_responsibility_pattern.LengthValidationHandler

::: src.advanced.chain_of_responsibility_pattern.PrefixValidationHandler

::: src.advanced.chain_of_responsibility_pattern.SuffixValidationHandler

::: src.advanced.chain_of_responsibility_pattern.ContentValidationHandler

## Chain of Responsibility

Initializes an instance of the class that defines
  the current handler and the order of execution. The responsibility is to know
  when to use the handler, not how to handle it.

::: src.advanced.chain_of_responsibility_pattern.ChainOfResponsibility

Some real world applications of the chain of responsibility pattern are: User
journeys, logging systems, request processing, authentication/authorization,
data validation...

## Common Pitfalls

- **Broken Chain**: Forgetting to call the next handler breaks the chain. Always
  call the next handler unless explicitly terminating the chain.

```python
class GoodHandler(Handler):
    def handle(self, line: str) -> None:
        if some_condition:
            process(line)
        if self.next:  # Check next exists
            self.next.handle(line)
```

- **Circular References**: Creating a circular chain causes infinite recursion.
  Design your chain as a directed acyclic graph (DAG). Test for cycles if
  handlers can be dynamically configured.

- **Exception Handling**: Exceptions in one handler can prevent other handlers
  from executing. Plan your exception strategy properly. Should exceptions stop
  the chain or should handlers catch and pass them along?

- **Order Dependencies**: The order of handlers can affect the outcome. Document
  the expected order by defining and documenting clearly the flow.

- **Tight Coupling**: Use dependency injection to pass handlers, keeping them
  loosely coupled. Handlers that directly reference specific next handler types
  become tightly coupled.
