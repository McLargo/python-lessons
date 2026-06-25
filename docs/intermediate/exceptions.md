# Exceptions

<!-- markdownlint-disable MD046 -->
!!! info "Quality Score"
    **Overall Score**: 8.6/10 ✅ Excellent

    - Technical Accuracy: 28/35
    - Code Quality: 24/25
    - Educational Value: 21/25
    - Documentation: 13/15

    Last reviewed: June 25, 2026
<!-- markdownlint-enable MD046 -->

Exceptions are a mechanism for handling errors in Python (and most programming
languages). When an error occurs when running a piece of code, Python raises an
exception. There are multiple types of exceptions (built-in and custom).
`BaseException` is the base class for all built-in exceptions, but commonly used
exceptions inherit from `Exception`. You can also create your own custom
exceptions by inheriting from `Exception` or any of its subclasses.

If the exception is not caught, the program will terminate immediately, raising
the corresponding exception and traceback.

::: src.intermediate.exceptions.exception_uncontrolled

Always raise proper exception when building your python code. It will help you
and your team to understand the error and how to fix it. A proper
module/library, should implement a consistent and robust mechanism to raise
exceptions, including in the docstrings sections of the module.

## Controlling exceptions

Exceptions can be caught and handled using a `try` block. You can catch the
exception, do something (like logging, metrics...), and continue running the
program.

::: src.intermediate.exceptions.exception_controlled

You can catch the exception, logging and raise the same exception to terminate
the execution.

::: src.intermediate.exceptions.exception_controlled_raise_exception

Similar way, you can catch the exception, logging and raise another your custom
exception (always use `from` to preserve the original exception context). You
can terminate the execution of a running program by raising an exception at any
time.

::: src.intermediate.exceptions.exception_controlled_raise_custom_exception

With the finally block, you can run code that will always run, regardless if the
code in the try block raises an exception. It will be always executed.

::: src.intermediate.exceptions.exception_with_finally

Adding the `else` block, you can run code that will only run if the code in the
try block does not raise an exception. It will be executed only if the try block
succeeds.

::: src.intermediate.exceptions.exception_with_else

Multiple exceptions can be caught in a single `except` block by specifying a
tuple of exception types. This is useful when you want to handle different
exceptions in the same way.

::: src.intermediate.exceptions.multiple_exceptions_controlled

You can also create your own custom exceptions, by inheriting from `Exception`
or any of its subclasses. This allows you to create exceptions that are specific
to your application or library. You can also add custom attributes and methods
to your custom exceptions, enriching the information that can be provided when
the exception is raised.

::: src.intermediate.exceptions.CustomError
    options:
      members:
        - CustomError

## Common pitfalls

Do not catch `Exception` or `BaseException` unless you have a very good reason
and you have great observability of your code. Catching these exceptions can
hide bugs and make it difficult to debug your code. The best approach is to
catch the exceptions that you expect to occur and handle them appropriately, and
let the unexpected exceptions propagate all the way up.

## References

- [Concrete exceptions](https://docs.python.org/3/library/exceptions.html#concrete-exceptions)
