# dict vs defaultdict

Inspect the difference between a `dict` and a `defaultdict` in Python.

## Access dict by key with square brackets

The easiest way to access a value inside dictionary is with **[key]** syntax.
But be careful, if the key does not exist, you will get a `KeyError`.

::: src.beginner.dict_vs_defaultdict.get_value_from_dict_with_square_brackets
    options:
      show_root_heading: true

## Access dict by key with get method

Using `get` method is another option. If key is not present in dict, None (or
custom value) is returned.

::: src.beginner.dict_vs_defaultdict.get_value_from_dict_with_get
    options:
      show_root_heading: true

## Use defaultdict

**defaultdict** enables a dict with a default value, even if requested with
square brackets. When setting `defaultdict`, you can send as first argument
(`default_factory`) a function that will be called when key is not present in
dict . String, int, list, None... any type you want. If you don't set
`default_factory`, KeyError will be raised if key is not present.

::: src.beginner.dict_vs_defaultdict.get_value_from_defaultdict
    options:
      show_root_heading: true

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
