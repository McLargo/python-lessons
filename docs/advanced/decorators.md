# Decorators

A decorator is a design pattern in Python that allows to add new functionality
to an existing object or function without modifying its structure.

Very useful when the same functionality is required in different places, as it
is very simple to reuse without having to copy and paste the code. Very easy to
maintain.

## Measure decorator

The measure decorator is a very simple example of a decorator. It allows to
measure the time it takes to execute a function.

::: src.advanced.decorators.measure.measure

## Retry decorator

The retry decorator is a more complex example of a decorator. It allows to retry
a function a number of times if it fails.

:::src.advanced.decorators.retry.retry

## Singleton decorator

The singleton decorator is a very useful example of a decorator. It allows to
ensures that only exists one instance of a class.

:::src.advanced.decorators.singleton.singleton
