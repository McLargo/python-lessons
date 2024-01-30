# Lambda functions

Lambda expressions are ideally used when we need to do something simple and are
more interested in getting the job done quickly rather than formally naming the
function.

Lambda expressions are also known as anonymous functions.

Lambda functions behave like normal functions declared with the def keyword.
They are useful when you want to define a small function concisely.
They must contain only one expression, so they are not best suited for functions
with control flow statements.

## Misused

Lambda functions help to write is just one line, code that would require a
bunch of lines.
It can make the code less readable. They are very useful, but overuse can make
the code difficult to understand.

## Use with functions like map(), max(), etc

Functions like map() can be used with lambda functions. In that case, map() will
the lambda function to every element of a given iterable (list, tuple, etc.).

For example:

::: src.advanced.lambda_functions.get_list_of_fields_from_a_list_dict

## Apply lambda functions for sorting data

Lambda functions can be used for sorting dada in list, dict, etc.

::: src.advanced.lambda_functions.sort_a_list_of_dict_by_a_field

## Pass a lambda function as parameter to a function

::: src.advanced.lambda_functions.filter_by_applying_function_to_elements
