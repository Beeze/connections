def get_class_attributes(class_obj):
    return ([attribute for attribute in dir(class_obj)
             if not attribute.startswith('_')
             and not attribute.endswith('_')
             and not attribute.startswith('init')])

def both_classes_have_none_null_attributes(c1, c2, attribute):
    return (hasattr(c1, attribute)
            and hasattr(c2, attribute)
            and getattr(c1, attribute) is not None
            and getattr(c2, attribute) is not None)


def is_one_class_with_attribute(c1, c2, attribute):
    return hasattr(c1, attribute) or hasattr(c2, attribute)


def get_attribute_from_class(c1, c2, attribute):
    return getattr(c1, attribute) if hasattr(c1, attribute) else getattr(c2, attribute)
