from __future__ import annotations

import abc
from typing import Type

from latexpy.core.base import AbstractElement, AbstractVisitable
from latexpy.util.decorator import require_type
from latexpy.core.iterator import PreorderIterator
from latexpy.util.misc import upper_bound_inherit_tree


class Tex(AbstractElement, AbstractVisitable):
    """
    """

    _parent = None

    def __init__(self, autoadd=False):
        super().__init__()
        self._children = []
        if autoadd:
            self.parent.add(self)

    @require_type(1, AbstractElement)
    def _add(self, child: AbstractElement) -> None:
        self._children.append(child)

    def _remove(self, child: AbstractElement) -> None:
        self._children.remove(child)

    def __enter__(self):
        self._original_parent = self.parent
        self.parent = self
        return self

    def __exit__(self, type_, value, traceback):
        self.parent = self._original_parent

    def __iter__(self):
        yield from PreorderIterator(self)


    @property
    def children(self):
        return self._children

    @property
    def prefix(self):
        return ""

    @property
    def suffix(self):
        return ""

    @property
    def parent(self):
        return Tex._parent

    @parent.setter
    def parent(self, parent: Tex):
        Tex._parent = parent

    def __str__(self):
        return self.prefix + self.suffix


class Options(Tex):
    def __init__(self, autoadd):
        super().__init__(autoadd)


class SquareBracket(Options):
    def __init__(self, autoadd):
        super().__init__(autoadd)

    @property
    def prefix(self):
        return "["

    @property
    def suffix(self):
        return "]"


class CurlyBracket(Options):
    def __init__(self, autoadd):
        super().__init__(autoadd)

    @property
    def prefix(self):
        return "{"

    @property
    def suffix(self):
        return "}"


class Star(Options):
    def __init__(self, autoadd=True):
        super().__init__(autoadd)

    @property
    def prefix(self):
        return "*"


class CallableElement(Tex):

    _name = ""

    def __init__(self, autoadd=True):
        super().__init__(autoadd)

    @property
    def name(self):
        return self._name

    @property
    def prefix(self):
        return ""

    @property
    def suffix(self):
        return ""


class Environment(CallableElement):
    def __init__(self, autoadd=True):
        super().__init__(autoadd)

    @property
    def prefix(self):
        return r"\begin{{{}}}".format(self.name) + "%\n"

    @property
    def suffix(self):
        return r"\end{{{}}}".format(self.name) + "%\n"


class Function(CallableElement):
    def __init__(self, autoadd=True):
        super().__init__(autoadd)

    @property
    def prefix(self):
        return "\\" + self.name + "%\n"

    @property
    def suffix(self):
        return ""


class PlainText(Tex):
    def __init__(self, autoadd=True):
        super().__init__(autoadd)


class Section(Function):
    _name = "section"


class Subsection(Function):
    _name = "subsection"


class Enumerate(Environment):
    _name = "enumerate"


class Itemize(Environment):
    _name = "itemize"


class Item(Function):
    _name = "item"


class Documentclass(Function):
    _name = "documentclass"


class Document(Environment):
    _name = "document"


class Figure(Environment):
    _name = "figure"


class Tabular(Environment):
    _name = "tabular"


class Package(Function):
    _name = "usepackage"


__all__ = [cls.__name__ for cls in upper_bound_inherit_tree(Tex)]
