import pytest

from latexpy.core.element import Tex, CallableElement

def test_tex_add():

    f = Tex()
    g = Tex()
    h = CallableElement()
    
    f._add(g)

    with pytest.raises(TypeError):
        f._add(45)

    f._add(h)

    assert f._children == [g, h]
