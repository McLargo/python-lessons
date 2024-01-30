"""Module to check if an instance is of a given type.

This module contains a function to check if an instance is of a given type.

"""


def is_instance(instance, instance_type) -> bool:
    """Check if instance is of the type provided.

    Parameters:
        instance (object): any kind of object.
        instance_type (class or tuple): expected instance type for instance.

    Returns:
        bool: true if instance is the one expected, false otherwise.
    """
    return isinstance(instance, instance_type)
