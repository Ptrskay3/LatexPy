from typing import Union, Callable, Type

from latexpy.core.base import AbstractElement
from latexpy.util.decorator import require_type


class Tex(AbstractElement):
    """
    """
    def __init__(self):
        super().__init__()
        self._children = []

    @require_type(1, AbstractElement)
    def _add(self, child: AbstractElement) -> None:
        self._children.append(child)

    def _remove(self, child: AbstractElement) -> None:
        self._children.remove(child)

    def __iter__(self):
        return self # will be rewritten

    def accept(self, visitor):
        pass

    def children_iterator(self):
        return self.children

    @property
    def children(self):
        return self._children


class CallableElement(Tex):

    _name = ""

    def __init__(self):
        super().__init__()

    @property
    def name(self):
        return self._name


class Environment(CallableElement):
    def __init__(self):
        super().__init__()


class Function(CallableElement):
    def __init__(self):
        super().__init__()


class PlainText(Tex):
    def __init__(self):
        super().__init__()


def class_factory(name: str, inherit_from: Type=Function) -> Type:
    class cls(inherit_from):
        _name = name

    cls.__name__ = name.title()
    return cls


# all the similar elements should be defined here

Package = class_factory("package")
Enumerate = class_factory("enumerate")
Itemize = class_factory("itemize")
Figure = class_factory("figure")
Tabular = class_factory("tabular")
