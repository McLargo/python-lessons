# Dataclasses

<!-- markdownlint-disable MD046 -->
!!! info "Quality Score"
    **Overall Score**: 8.7/10 ✅ Excellent

    - Technical Accuracy: 28/35
    - Code Quality: 23/25
    - Educational Value: 22/25
    - Documentation: 14/15

    Last reviewed: June 22, 2026
<!-- markdownlint-enable MD046 -->

Dataclasses are a new feature in Python 3.7. They are a convenient way to create
classes which are mainly used to store data. By default, dataclasses provide a
`__repr__` and `__init__` method, so we don't have to write them ourselves.

::: src.beginner.dataclass
    options:
      members:
        - Circle

## Properties

Dataclasses can have properties, which are computed attributes. They are defined
by using the `@property` decorator. And they can be used like normal attributes,
without parentheses.

## `*args` and `**kwargs`

Methods can be called with `*args` and `**kwargs`. `*args` represents a tuple of
positional arguments, and `**kwargs` represents a dict of keyword arguments.
This is useful when we want to pass a variable number of arguments to a method,
or when we want to capture arguments that we don't know about.

## Common pitfalls

Remember to avoid using mutable default values for dataclass fields. They are
shared across all instances of the dataclass, which can lead to unexpected
behavior.

```python
# bad example
@dataclass
class Team:
    name: str
    members: list = []

# correct example
from dataclasses import dataclass, field

@dataclass
class Team:
    name: str
    members: list = field(default_factory=list)
```

## References

- [Dataclasses](https://docs.python.org/3/library/dataclasses.html)
- [PEP 557](https://peps.python.org/pep-0557/)
