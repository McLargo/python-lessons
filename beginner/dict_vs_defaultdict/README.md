### 1. dict type

```
default_dict = {"key": "value"}
print(default_dict["key"])
```

```
# In case of key not present on dict, KeyError exception is raised
print(default_dict["other_key"])
```

```
# You can control KeyError exception
try:
    print(default_dict["other_key"])
except KeyError:
    print('default_value')
```

```
# to avoid KeyError, you can use conditional
if "key" in default_dict:
    print(default_dict["key"])
if "other_key" in default_dict:
    print(default_dict["other_key"])
```

```
# or use `get` method. If key is not present in dict, None (or custom value) is returned
print(default_dict.get("key"))
print(default_dict.get("other_key"))
print(default_dict.get("other_key", "default_value"))
```

### 2. defaultdict

```
from collections import defaultdict

col_default_dict = defaultdict(lambda: None)
col_default_dict.update({"key": "value"})
print(col_default_dict["key"])  # expected `value`
print(col_default_dict["other_key"])  # expected `None`

col_default_dict_int = defaultdict(int)
col_default_dict_int.update({"key": 22})
print(col_default_dict_int["key"])  # expected '22'
print(col_default_dict_int["other_key"])  # expected 0

col_default_dict_list = defaultdict(list)
col_default_dict_list["key"] = [1, 2, 3]
print(col_default_dict_list["key"])  # expected `[1,2,3]`
print(col_default_dict_list["other_key"])  # expected `[]`
```

### 3. Performance

```
from timeit import timeit

print("Get missing default dict:", timeit(
    stmt="default_dict.get('key')",
    setup="default_dict = {}",
    number=5000000))

print("Get missing collection default dict:", timeit(
    stmt="default_dict['key']",
    setup="from collections import defaultdict; default_dict = defaultdict(lambda: None)",
    number=5000000))
```

### 4. Storage

```
import sys

print(sys.getsizeof(dict()))
print(sys.getsizeof(defaultdict(lambda: None)))
```

### 5. Bibliografy
More information https://realpython.com/python-defaultdict/#defaultdict-vs-dictsetdefault


