# Decorators

<!-- markdownlint-disable MD046 -->
!!! info "Quality Score"
    **Overall Score**: 9.1/10 ⭐ Excellent

    - Technical Accuracy: 30/35
    - Code Quality: 25/25
    - Educational Value: 22/25
    - Documentation: 14/15

    Last reviewed: June 22, 2026
<!-- markdownlint-enable MD046 -->

A decorator is a structural design pattern in Python that allows to add new
functionality to an existing object or function without modifying its structure.

Very useful when the same functionality is required in different places, as it
is very simple to reuse without having to copy and paste the code. Very easy to
maintain and extend, as it allows to add new functionality without modifying the
existing code.

## Key features of decorators

- Multiple decorators can be applied to a single function or method, separating
  concerns and maintaining a clean and readable codebase.
- They are applied from bottom to top. Last defined decorator is the first to
  be applied.
- Parametrized, allowing to customize their behavior without having to define
  multiple decorators for each case.

There are common use cases for decorators, such as logging, measuring execution
time, retrying, authentication, caching...

## Measure decorator

The measure decorator is a very simple example of a decorator. It allows to
measure the time it takes to execute a function.

::: src.advanced.decorators.measure

## Retry decorator

The retry decorator is a more complex example of a decorator. It allows to retry
a function a number of times if it fails.

::: src.advanced.decorators.retry

## Singleton decorator

The singleton decorator is a very useful example of a decorator. It allows to
ensures that only exists one instance of a class.

::: src.advanced.decorators.singleton

## Common pitfalls

Remember to use `functools.wraps` to preserve the original function's metadata,
such as its name, docstring, and module. This is important for debugging and
introspection.
