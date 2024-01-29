"""Singleton decorator.

This method is a decorator to ensures that only exists one instance of a class.

"""


def singleton(cls: type):
    """Singleton decorator.

    Method to decorate a class as a singleton. This decorator ensures that
    exists only one instance of a class.

    Args:
        cls (type): Class to decorate

    Returns:
        (type): Instance of the decorated class
    """

    def __new__singleton(cls: type, *args, **kwargs):  # noqa: ARG001
        if not hasattr(cls, "__singleton"):
            cls.__singleton = object.__new__(cls)
        return cls.__singleton

    cls.__new__ = __new__singleton
    return cls
