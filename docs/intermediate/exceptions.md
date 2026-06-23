# Exceptions

<!-- markdownlint-disable MD046 -->
!!! info "Quality Score"
    **Overall Score**: 7.1/10 ⚠️ Good/Needs Work

    - Technical Accuracy: 20/35
    - Code Quality: 18/25
    - Educational Value: 22/25
    - Documentation: 11/15

    Last reviewed: June 22, 2026
<!-- markdownlint-enable MD046 -->

Exceptions are a mechanism for handling errors in Python (and most programming
language). When an error occurs when running your code, Python raises an
exception. There are multiple types of exceptions. Each exception has a name and
a message.

If the exception is not caught, the program will terminate immediately, raising
the corresponding exception.

::: src.intermediate.exceptions.exception_uncontrolled

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

## Common pitfalls

Do not catch `Exception` or `BaseException` unless you have a very good reason
and you have great observability of your code. Catching these exceptions can
hide bugs and make it difficult to debug your code. The best approach is to
catch the exceptions that you expect to occur and handle them appropriately, and
let the unexpected exceptions propagate all the way up.

## References

- [Concrete exceptions](https://docs.python.org/3/library/exceptions.html#concrete-exceptions)
