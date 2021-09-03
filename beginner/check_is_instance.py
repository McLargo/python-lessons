"""
Sample of a how to use `isinstance` method

"""


def is_instance(instance, instance_type):
    """Check if instance is type expected

    :param object: any kind of object
    :param class or tuple: expected instance_type for instance
    :returns: True/False if check of instance is correct
    :rtype: bool
    """
    return isinstance(instance, instance_type)
