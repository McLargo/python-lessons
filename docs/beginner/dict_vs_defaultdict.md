# dict vs defaultdict

<!-- markdownlint-disable MD046 -->
!!! info "Quality Score"
    **Overall Score**: 8.1/10 ✅ Good

    - Technical Accuracy: 28/35
    - Code Quality: 20/25
    - Educational Value: 20/25
    - Documentation: 13/15

    Last reviewed: June 22, 2026
<!-- markdownlint-enable MD046 -->

Inspect the difference between a `dict` and a `defaultdict` in Python.

## Access dict by key with square brackets

The easiest way to access a value inside dictionary is with **[key]** syntax.
But be careful, if the key does not exist, you will get a `KeyError`.

::: src.beginner.dict_vs_defaultdict.get_value_from_dict_with_square_brackets

## Access dict by key with get method

Using `get` method is another option. If key is not present in dict, None (or
custom value) is returned.

::: src.beginner.dict_vs_defaultdict.get_value_from_dict_with_get

## Use defaultdict

**defaultdict** enables a dict with a default value, even if requested with
square brackets. When setting `defaultdict`, you can send as first argument
(`default_factory`) a function that will be called when key is not present in
dict . String, int, list, None... any type you want. If you don't set
`default_factory`, KeyError will be raised if key is not present.

::: src.beginner.dict_vs_defaultdict.get_value_from_defaultdict

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

## Common pitfalls

`defaultdict` creates a new entry in the dictionary when you access a missing
key. This can lead to unexpected behavior if you are not careful.
