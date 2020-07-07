from __future__ import annotations

import abc
from collections.abc import Iterable
from typing import Union, Iterator, Type, Callable, Iterable as _iterable


class AbstractElement(Iterable, abc.ABC):
    """
    """

    @abc.abstractmethod
    def _add(self, child: AbstractElement) -> None:
        """
        """
        pass

    def add(self, children: Union[AbstractElement, Iterator]) -> None:
        """
        """
        pass

    @abc.abstractmethod
    def accept(self, visitor: AbstractVisitor) -> None:
        """
        """
        pass

    @abc.abstractmethod
    def children_iterator(self) -> _iterable:
        """
        """
        pass


class AbstractVisitor():
    """
    """

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        for key, value in AbstractVisitor._visit_functions.items():
            setattr(cls, "_visit_" + key.__name__.lower(), value)
        delattr(AbstractVisitor, "_visit_functions")
        

    def visit(self, visitable: AbstractVisitable) -> None:
        getattr(self, "_visit_" + type(visitable).__name__.lower())(visitable)

    @classmethod
    def collect_visitable(cls, klass: Type) -> Callable:
        def wrapper(func: Callable) -> Any:
            val = getattr(AbstractVisitor, "_visit_functions", {})
            val.update({klass: func})
            AbstractVisitor._visit_functions = val
            return func
        return wrapper


class AbstractVisitable():

    def accept(self, visitor: AbstractVisitor) -> None:
        visitor.visit(self)
