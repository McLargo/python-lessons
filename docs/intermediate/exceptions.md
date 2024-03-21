# Exceptions

Exceptions are a mechanism for handling errors in Python (and most programming
language). When an error occurs when running your code, Python raises an
exception. There are multiple types of exceptions. Each exception has a name and
a message.

If the exception is not caught, the program will terminate immediately, raising
the corresponding exception.

::: src.intermediate.exceptions.exception_uncontrolled

## Controlling exceptions

Exceptions can be caught and handled using a `try` block. You can catch the
exception, do something (like logging), and continue running the program.

::: src.intermediate.exceptions.exception_controlled

You can catch the exception, logging and raise the same exception to terminate
the execution.

::: src.intermediate.exceptions.exception_controlled_raise_exception

Similar way, ou can catch the exception, logging and raise another type of
exception. You can terminate the execution of a running program by raising an
exception at any time.

::: src.intermediate.exceptions.exception_controlled_raise_custom_exception

With the finally block, you can run code that will always run, regardless if the
code in the try block raises an exception. It will be always executed.

::: src.intermediate.exceptions.exception_controlled_raise_custom_exception

## References

- [Concrete exceptions](https://docs.python.org/3/library/exceptions.html#concrete-exceptions)
