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

    def add(self, children: Union[AbstractElement, _iterator]) -> None:
        """
        """
        pass

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
