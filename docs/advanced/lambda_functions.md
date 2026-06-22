# Lambda functions

Lambda expressions are ideally used when we need to do something simple and are
more interested in getting the job done quickly rather than formally naming the
function.

Lambda expressions are also known as anonymous functions.

Lambda functions behave like normal functions declared with the `def` keyword.
They are useful when you want to define a small function concisely. This limit
the usage to single expression, without statements and without type hints.
Usually, best used is for sorting, filtering or mapping data. Do not use more
than one line or expression, that is consider a bad practice.

Lambda functions should not be used for complex logic, when
debugging/observability is required or reusability is a concern. In those cases,
it is better to use a normal function declared with the `def` keyword.

## Performance and readability

Lambda functions have no impact on performance compared to normal methods (`def`
functions). Well written, lambda functions can be more readable than normal
functions, especially when the function is simple and context is clear. If
readability is a concern, it is better to use a normal function.

## Use with functions like map(), max(), etc

Functions like `map` can be used with lambda functions. In that case, `map` will
apply the lambda function to every element of a given iterable (list, tuple,
etc.).

For example:

::: src.advanced.lambda_functions.get_list_of_fields_from_a_list_dict

## Apply lambda functions for sorting data

Lambda functions can be used for sorting data in list, dict, etc.

::: src.advanced.lambda_functions.sort_a_list_of_dict_by_a_field

## Pass a lambda function as parameter to a function

Lambda functions can be passed as parameters to other functions. This is useful
when we want to customize the behavior of a function without having to define a
new function.

::: src.advanced.lambda_functions.filter_by_applying_function_to_elements

## Lambda gotchas

One common issue is related to usage of lambda functions in loops, where the
lambda function captures the variable by reference, not by value. This can lead
to unexpected behavior when the lambda function is executed later.

```python

# bad example: Lambda captures variable by reference
functions = []
for i in range(5):
    functions.append(lambda: i)

# good example: Use default argument to capture by value
functions = []
for i in range(5):
    functions.append(lambda i=i: i)
```

Another gotcha is related to late binding, where the lambda function uses the
value of a variable at the time the function is called, not at the time the
function is defined.

```python
# bad example: Lambda uses variable value at call time
multiplier = 2
multiply = lambda x: x * multiplier

# good example: Use a regular function for clarity
def create_multiplier(multiplier):
    return lambda x: x * multiplier
```
