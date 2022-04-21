### 1. dict type

The easiest way to access a value inside dictionary is with [key]
```
In [1]: default_dict = {"key": "value"}

In [2]: print(default_dict["key"])
value
```

In case of key not present on dict, KeyError exception is raised
```
In [3]: print(default_dict["other_key"])
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-3-b8141f1d53f7> in <module>
----> 1 print(default_dict["other_key"])

KeyError: 'other_key'
```

You can control KeyError exception
```
In [4]: try:
   ...:     print(default_dict["other_key"])
   ...: except KeyError:
   ...:     print('default_value')
   ...:
default_value
```

to avoid KeyError, you can use a conditional
```
In [5]: if "key" in default_dict:
   ...:     print(default_dict["key"])
   ...: if "other_key" in default_dict:
   ...:     print(default_dict["other_key"])
   ...:
value
```

Other option is use `get` method. If key is not present in dict, None (or custom value) is returned
```
In [6]: print(default_dict.get("key"))
value

In [7]: print(default_dict.get("other_key"))
None

In [8]: print(default_dict.get("other_key", "default_value"))
default_value
```

### 2. defaultdict

defaultdict enables a dict with a default value.
Useful in the occasions where you need a default value always. String, int, list, None...

```
In [9]: from collections import defaultdict

In [10]: col_default_dict = defaultdict(lambda: None)
    ...: col_default_dict.update({"key": "value"})
    ...: print(col_default_dict["key"])  # expected `value`
    ...: print(col_default_dict["other_key"])  # expected `None`
value
None

In [11]: col_default_dict_int = defaultdict(int)
    ...: col_default_dict_int.update({"key": 22})
    ...: print(col_default_dict_int["key"])
    ...: print(col_default_dict_int["other_key"])
22
0

In [12]: col_default_dict_list = defaultdict(list)
    ...: col_default_dict_list["key"] = [1, 2, 3]
    ...: print(col_default_dict_list["key"])
    ...: print(col_default_dict_list["other_key"])
[1, 2, 3]
[]
```

### 3. Performance

Great performance in using default_dict vs get

```
In [13]: from timeit import timeit

In [14]: print("Get missing default dict:", timeit(
    ...:     stmt="default_dict.get('key')",
    ...:     setup="default_dict = {}",
    ...:     number=5000000))
Get missing default dict: 0.2938706480017572

In [15]: print("Get missing collection default dict:", timeit(
    ...:     stmt="default_dict['key']",
    ...:     setup="from collections import defaultdict; default_dict = defaultdict(lambda: None)",
    ...:     number=5000000))
    ...:
Get missing collection default dict: 0.16622997199738165
```

### 4. Storage

Relative bigger size of dict, but not really that much
```
In [16]: import sys

In [17]: print(sys.getsizeof(dict()))
248

In [18]: print(sys.getsizeof(defaultdict(lambda: None)))
256
```

### 5. Bibliografy
More information https://realpython.com/python-defaultdict/#defaultdict-vs-dictsetdefault


