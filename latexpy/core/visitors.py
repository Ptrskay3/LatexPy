from latexpy.core.base import AbstractVisitor
from latexpy.core.element import Tex
from latexpy.util.misc import upper_bound_inherit_tree

class AbstractTexVisitor(AbstractVisitor):
    def __init_subclass__(cls, **kwargs):
        defined_classes = upper_bound_inherit_tree(Tex)
        for defined_class in defined_classes:
            if defined_class.__name__.lower()


class DefaultChildIndentVisitor(AbstractTexVisitor):
    defaults = {Tex:0,}

    def __init__(self):
        self.is_valid()

    def is_valid(self):
        defined_classes = upper_bound_inherit_tree(Tex)
        for key, value in DefaultChildIndentVisitor.defaults.items():
            defined_classes.pop(key)

        if defined_classes:
            raise ValueError("Must specify all default indents.")

