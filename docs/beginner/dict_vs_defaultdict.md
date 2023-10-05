# dict vs defaultdict

Inspect the difference between a `dict` and a `defaultdict` in Python.

## Access dict by key with square brackets

The easiest way to access a value inside dictionary is with **[key]** syntax.
But be careful, if the key does not exist, you will get a `KeyError`.

::: src.beginner.dict_vs_defaultdict
    options:
      members:
        - get_value_from_key_with_square_brackets

## Access dict by key with get method

Using `get` method is another option. If key is not present in dict, None (or
custom value) is returned.

::: src.beginner.dict_vs_defaultdict
    options:
      members:
        - get_value_from_key_with_get

## Use defaultdict

**defaultdict** enables a dict with a default value. Useful in the occasions
where you need a default value always. String, int, list, None... any type you want.

::: src.beginner.dict_vs_defaultdict
    options:
      members:
        - get_value_from_defaultdict

## Performance comparison

There is a great performance in using defaultdict vs get

```python
from timeit import timeit

print("Get missing default dict:", timeit(
    stmt="default_dict.get('key')",
    setup="default_dict = {}",
    number=5000000)
)
Get missing default dict: 0.1267744980000316

print("Get missing collection default dict:", timeit(
    stmt="default_dict['key']",
    setup="from collections import defaultdict; default_dict = defaultdict(lambda: None)",  # noqa
    number=5000000)
)
Get missing collection default dict: 0.0706390929999543

```
