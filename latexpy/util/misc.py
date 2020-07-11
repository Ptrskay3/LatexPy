from typing import Type, Set


def upper_bound_inherit_tree(upper_bound_class: Type) -> Set[Type]:
    classes = {upper_bound_class}
    work = [upper_bound_class]
    while work:
        parent = work.pop()
        for child in parent.__subclasses__():
            if child not in classes:
                classes.add(child)
                work.append(child)

    return classes
