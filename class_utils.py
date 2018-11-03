import inspect


def get_class_attributes(class_obj):
    attributes = inspect.getmembers(class_obj, lambda a: not(inspect.isroutine(a)))
    return [a for a in attributes if not(a[0].startswith('__') and a[0].endswith('__'))]


def both_classes_have_none_null_attributes(c1, c2, attribute):
    return (hasattr(c1, attribute)
            and hasattr(c2, attribute)
            and getattr(c1, attribute) is not None
            and getattr(c2, attribute) is not None)


def is_one_class_with_attribute(c1, c2, attribute):
    return hasattr(c1, attribute) or hasattr(c2, attribute)


def get_attribute_from_class(c1, c2, attribute):
    return getattr(c1, attribute) if hasattr(c1, attribute) else getattr(c2, attribute)
