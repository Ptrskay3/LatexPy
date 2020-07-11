from latexpy.core.base import AbstractVisitor
from latexpy.core.element import *
from latexpy.util.misc import upper_bound_inherit_tree


class AbstractTexVisitor(AbstractVisitor):
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__()
        AbstractVisitor.__init_subclass__(**kwargs)
        defined_classes = upper_bound_inherit_tree(Tex)
        for defined_class in defined_classes:
            if not hasattr(cls, AbstractVisitor.get_function_name(defined_class)):
                raise ValueError(
                    f"Must specify all default indents for {AbstractVisitor.get_function_name(defined_class)}"
                )


class DefaultChildrenIndentVisitor(AbstractTexVisitor):
    tab = "(TAB)"
    defaults = {
        Tex: False,
        Star: False,
        CallableElement: False,
        CurlyBracket: False,
        Enumerate: tab,
        Subsection: "",
        Section: "",
        Documentclass: False,
        Document: False,
        SquareBracket: False,
        Package: False,
        Tabular: tab,
        Item: False,
        Figure: tab,
        Itemize: tab,
        Function: False,
        PlainText: False,
        Options: False,
        Environment: False,
    }
