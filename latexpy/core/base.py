from __future__ import annotations

import abc
from collections.abc import Iterable
from typing import Union, Iterable, Iterator as _iterator 


class AbstractElement(Iterable, abc.ABC):
    """
    """
    @abc.abstractmethod
    def _add(self, child: AbstractElement) -> None:
        """
        """
        pass

    @abc.abstractmethod
    def _remove(self, child: AbstractElement) -> None:
        """
        """
        pass


    def add(self, children: Union[AbstractElement, _iterator]) -> None:
        if isinstance(children, AbstractElement):
            self._add(children)
        elif isinstance(children, Iterable):
            for child in children:
                self._add(child)
        else:
            raise TypeError

    def remove(self, children: Union[AbstractElement, _iterator]) -> None:
        if isinstance(children, AbstractElement):
            self._remove(children)
        elif isinstance(children, Iterable):
            for child in children:
                self._remove(child)
        else:
            raise TypeError

    @abc.abstractmethod
    def accept(self, visitor: AbstractVisitor) -> None:
        """
        """
        pass

    @abc.abstractmethod
    def children_iterator(self) -> Iterable:
        """
        """
        pass


class AbstractVisitor(abc.ABC):
    """
    """
    @abc.abstractmethod
    def visit(self, element: AbstractElement) -> None:
        pass
