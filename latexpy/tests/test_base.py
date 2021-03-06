import pytest

from latexpy.core.base import AbstractElement, AbstractVisitor


# TODO : add more test cases
@pytest.mark.parametrize("inherit_from", [AbstractElement])
def test_baseclass(inherit_from):
    class FailClass(inherit_from):
        pass

    with pytest.raises(TypeError):
        FailClass()


def test_abstractvisitor():
    class WorkingClass(AbstractVisitor):
        @AbstractVisitor.mark_visitable(object)
        def visit(self, attr):
            pass

    WorkingClass()


def test_abstractelement():
    class WorkingClass(AbstractElement):
        def _add(self, child):
            pass

        def accept(self, visitor):
            pass

        @property
        def children(self):
            pass

        def __iter__(self):
            pass

        def _remove(self, child):
            pass

    WorkingClass()


def test_abstractelement_add():
    pass
