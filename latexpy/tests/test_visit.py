from unittest import mock
from unittest.mock import MagicMock

import pytest
from latexpy.core.base import AbstractVisitor, AbstractVisitable


class Alma:
    pass


class Narancs:
    pass


class Dinnye:
    pass


def test_visit():
    alma = Alma()
    Alma._visit_alma = MagicMock(name="_visit_alma")
    AbstractVisitor._visit_alma = MagicMock(name="_visit_alma")
    visitor = AbstractVisitor()
    visitor.visit(alma)
    AbstractVisitor._visit_alma.assert_called_with(alma)


# @pytest.mark.skip()
def test_rename():
    class Korte(AbstractVisitor):
        @AbstractVisitor.mark_visitable(Alma)
        def method(self, visitable):
            return "Alma"

        @AbstractVisitor.mark_visitable(Dinnye)
        def method(self, visitable):
            return "Dinnye"

    korte = Korte()
    assert korte.method(Alma) == "Dinnye"
    assert korte._visit_alma(Alma) == "Alma"
    assert korte._visit_alma(Dinnye) == "Alma"
    assert korte._visit_dinnye(Dinnye) == "Dinnye"
    assert korte._visit_dinnye(Alma) == "Dinnye"


def test_defaults():
    class Korte(AbstractVisitor):
        defaults = {Alma: 0, Dinnye: 2, Narancs: 3}

    korte = Korte()
    assert korte._visit_alma(Alma) == 0
    assert korte._visit_alma(Dinnye) == 0
    assert korte._visit_dinnye(Dinnye)
    assert korte._visit_dinnye(Alma)
