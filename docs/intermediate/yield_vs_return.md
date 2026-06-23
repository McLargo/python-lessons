# Yield vs return

## Return

`return` keyword implies the output of a function. It stops the function after
running.

::: src.intermediate.yield_vs_return.return_even_numbers

## Yield

`yield` keyword also returns a value, but a function can yield multiple outputs,
so it does not stop the entire function. Yield returns a generator object, which
is an iterator. It can be used in loops.

::: src.intermediate.yield_vs_return.yield_even_numbers

You can use yield instead of return when the data size is large, as it doesn't
store in memory the entire result, only when function is called. It is an
efficient way of producing data that is big or infinite.

::: src.intermediate.yield_vs_return.yield_fibonacci_numbers

Yield returns a generator object, which is an iterator. It can be used in loops.
After you initialize the generator, you can use `next()` to get the next value.
When there are no more values to yield, it raises `StopIteration` exception. The
generator can be used in a loop, and it will automatically stop when there are
no more values to yield.

Once a generator is exhausted, it cannot be reused. You need to create a new
generator object to iterate again.
