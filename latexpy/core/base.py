from __future__ import annotations

import abc
from collections.abc import Iterable
from copy import copy
from typing import Union, Iterator, Type, Callable, Any, Iterable as _iterable


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
        if isinstance(children, AbstractElement):
            self._add(children)
        elif isinstance(children, Iterable):
            for child in children:
                self._add(child)
        else:
            raise TypeError

    @abc.abstractmethod
    def _remove(self, child: AbstractElement) -> None:
        """
        """
        pass

    def remove(self, children: Union[AbstractElement, Iterator]) -> None:
        """
        """
        if isinstance(children, AbstractElement):
            self._remove(children)
        elif isinstance(children, Iterable):
            for child in children:
                self._remove(child)
        else:
            raise TypeError




    @property
    @abc.abstractmethod
    def children(self) -> _iterable:
        """
        """
        pass


class AbstractVisitor:
    """
    """

    @staticmethod
    def get_function_name(cls: Type):
        return "_visit_" + cls.__name__.lower()

    defaults: dict = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        for key, value in copy(cls.defaults).items():
            setattr(
                cls,
                AbstractVisitor.get_function_name(key),
                (lambda value: lambda self, visitable: value)(value),
            )
        if hasattr(AbstractVisitor, "_visit_functions"):
            for key, value in AbstractVisitor._visit_functions.items():
                setattr(cls, AbstractVisitor.get_function_name(key), value)
            delattr(AbstractVisitor, "_visit_functions")

    def visit(self, visitable: AbstractVisitable) -> Any:
        return getattr(self, AbstractVisitor.get_function_name(type(visitable)))(visitable)

    @classmethod
    def mark_visitable(cls, klass: Type) -> Callable:
        def wrapper(func: Callable) -> Any:
            val = getattr(AbstractVisitor, "_visit_functions", {})
            val.update({klass: func})
            AbstractVisitor._visit_functions = val
            return func

        return wrapper


class AbstractVisitable:
    def accept(self, visitor: AbstractVisitor) -> Any:
        return visitor.visit(self)
