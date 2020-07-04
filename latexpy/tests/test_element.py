import pytest

from latexpy.core.element import Tex, CallableElement


def test_tex_underscore_add():

    f = Tex()
    g = Tex()
    h = CallableElement()

    f._add(g)

    with pytest.raises(TypeError):
        f._add(45)

    f._add(h)

    assert f._children == [g, h]


def test_tex_underscore_remove():

    f = Tex()

    g = Tex()
    h = CallableElement()
    j = CallableElement()

    f._add(g)
    f._add(h)

    f._remove(g)
    assert f._children == [h]

    with pytest.raises(ValueError):
        f._remove(j)
