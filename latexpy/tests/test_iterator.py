import pytest

from latexpy.core.iterator import PreorderIterator, PostorderIterator
from latexpy.core.element import Tex


@pytest.fixture(scope="session")
def create_dummy_tree():
    class Dummy(Tex):
        def __init__(self, num):
            super().__init__()
            self.num = num

        def __str__(self):
            return str(self.num)

    dummy1 = Dummy(1)
    dummy2 = Dummy(2)
    dummy3 = Dummy(3)
    dummy4 = Dummy(4)
    dummy5 = Dummy(5)
    dummy6 = Dummy(6)
    dummy7 = Dummy(7)
    dummy1.add([dummy2, dummy3])
    dummy2.add([dummy4, dummy5])
    dummy3.add([dummy6, dummy7])
    return dummy1, Dummy


def test_preorder_iterator(create_dummy_tree):
    dummy, _ = create_dummy_tree
    expected = [1, 2, 4, 5, 3, 6, 7]
    assert expected == [d.num for d in PreorderIterator(dummy)]


def test_postorder_iterator(create_dummy_tree):
    dummy, _ = create_dummy_tree
    expected = [7, 6, 3, 5, 4, 2, 1]
    assert expected == [d.num for d in PostorderIterator(dummy)]
