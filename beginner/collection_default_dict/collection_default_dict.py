from collections import defaultdict

default_dict = defaultdict(lambda: None)
default_dict.update({"key": "value"})
print(default_dict["key"]) # expected 'value'
print(default_dict["key1"]) # expected None
