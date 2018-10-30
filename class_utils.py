import inspect


def get_class_attributes(class_obj):
    attributes = inspect.getmembers(class_obj, lambda a: not(inspect.isroutine(a)))
    return [a for a in attributes if not(a[0].startswith('__') and a[0].endswith('__'))]
