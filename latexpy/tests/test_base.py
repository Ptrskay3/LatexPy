import pytest

from latexpy.core.base import AbstractElement, AbstractVisitor


@pytest.mark.parametrize("inherit_from", [AbstractElement, AbstractVisitor])
def test_baseclass(inherit_from):
    class FailClass(inherit_from):
        pass

    with pytest.raises(TypeError):
        FailClass()


def test_abstractvisitor():
    class WorkingClass(AbstractVisitor):
        def visit(self, element):
            pass

    WorkingClass()


def test_abstractelement():
    class WorkingClass(AbstractElement):
        def _add(self, child):
            pass

        def accept(self, visitor):
            pass

        def children_iterator(self):
            pass

        def __iter__(self):
            pass

    WorkingClass()


def test_abstractelement_add():
    pass
