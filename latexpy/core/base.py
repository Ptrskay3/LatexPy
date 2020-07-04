from __future__ import annotations

import abc
from collections.abc import Iterable
from typing import Union, Iterator, Iterable as _iterable


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


class AbstractVisitor(abc.ABC):
    """
    """

    @abc.abstractmethod
    def visit(self, element: AbstractElement) -> None:
        pass
