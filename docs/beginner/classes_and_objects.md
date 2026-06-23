# Classes and objects

## Class

A class is the common structure for all objects or instances.

A class can have different methods and attributes:

- Static method: method that is bound to the class and not the object of the
  class.
- Class method: takes cls as the first parameter. It can modify a class state
  that would apply across all the instances of the class.
- Class attributes: Attributes that are common for all instances of the class.
  **Careful**, class attributes are mutable, that means, if value changes, it
  affects to all classes and objects. Use mainly for constants/default values
  and tracing data across all classes.

::: src.beginner.classes_and_objects
    options:
      members:
        - Pizza

## Object

An object is an instance of a class. It is a concrete entity based on arguments
during creation. Two objects of the same class are different, with or without
the same values.

## Common pitfalls

Do not use mutable objects as default values for the class creation or
arguments. They are shared across all instances of the class, and this is
usually something with unexpected effects, and it is hard to debug.

```python
# bad example
class Pizza:
    def __init__(self, toppings=[]):
        self.toppings = toppings

# correct example
class Pizza:
    def __init__(self, toppings=None):
        if toppings is None:
            toppings = []
        self.toppings = toppings
```
