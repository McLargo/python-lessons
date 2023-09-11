def is_instance(instance, instance_type) -> bool:
    """Check if instance is of the type provided.

    Parameters:
        instance (object): any kind of object.
        instance_type (class or tuple): expected instance_type for instance.

    Returns:
        bool: True if instance is the one expected, false otherwise.
    """
    return isinstance(instance, instance_type)
