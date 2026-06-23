# Check is instance

<!-- markdownlint-disable MD046 -->
!!! info "Quality Score"
    **Overall Score**: 9.5/10 ⭐ Outstanding

    - Technical Accuracy: 33/35
    - Code Quality: 25/25
    - Educational Value: 23/25
    - Documentation: 15/15

    Last reviewed: June 22, 2026
<!-- markdownlint-enable MD046 -->

Python is not a strong-typed language. This mean, that a variable can be
assigned to any type, even if previously it was assigned to another type.If
developers doesn't take care of this, it can lead to bugs and unexpected
behavior.

Python supports type hints in the code, but it is not enforced. Python provides
a built-in method called `isinstance`, that can be used to check if a variable
is of a certain type. It requires two arguments, the variable to be checked and
the type or tuple of types to be checked against. It returns `True` if the
variable is of the specified type, and `False`

::: src.beginner.check_is_instance
    options:
      members:
        - is_instance

This is useful because depending on the type, they offer different methods and
attributes. You can do `len` of a string, but not of an integer.

## Type

Another built-int method in python is `type`, that returns the type of variable.
It is not as flexible as `isinstance` because it only checks for the exact type,
and not for the subclasses (important when doing inheritance).

::: src.beginner.check_is_instance
    options:
      members:
        - is_instance_with_type

## Common pitfalls

There are some common pitfalls when using `isinstance`. `bool` is a subclass of
`int`, so if you check if a variable is an instance of `int`, it will return
`True` for a boolean variable. This can lead to unexpected behavior if you are
not aware of this.
