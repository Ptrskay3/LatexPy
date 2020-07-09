import pytest

from latexpy.core.element import (Tex, CallableElement, Documentclass,
    Package, Document, Section, Subsection, Figure, Itemize, Item)


@pytest.fixture()
def elements():
    f = Tex()
    g = Tex()
    h = CallableElement()
    j = CallableElement()
    k = CallableElement()
    return f, g, h, j, k

def test_tex_underscore_add(elements):

    f, g, h, j, _ = elements

    f._add(g)

    with pytest.raises(TypeError):
        f._add(45)

    f._add(h)

    assert f._children == [g, h]


def test_tex_add(elements):

    f, g, h, j, _ = elements

    f.add([g, j])

    with pytest.raises(TypeError):
        f._add(45)

    f._add(h)

    assert f._children == [g, j, h]

def test_tex_underscore_remove(elements):
    f, g, h, j, _ = elements

    f._add(g)
    f._add(h)

    f._remove(g)
    assert f._children == [h]

    with pytest.raises(ValueError):
        f._remove(j)

def test_tex_remove(elements):
    f, g, h, j, k = elements

    f.add([g, h, j])
    f.remove([g, j])

    assert f._children == [h]

    with pytest.raises(ValueError):
        f._remove(k)

def test_tree_construction():
    with Tex() as tex:
        tex.dummy = 1
        documentclass = Documentclass()
        documentclass.dummy = 2
        package = Package()
        package.dummy = 3
        with Document() as document:
            document.dummy = 4
            with Section() as section:
                section.dummy = 5
                figure = Figure()
                figure.dummy = 6
                with Itemize() as itemize:
                    itemize.dummy = 7
                    item1 = Item()
                    item1.dummy = 8
                    item2 = Item()
                    item2.dummy = 9
    
    tex = Tex(autoadd=False)
    tex.dummy = 1
    documentclass = Documentclass(autoadd=False)
    documentclass.dummy = 2
    package = Package(autoadd=False)
    package.dummy = 3
    document = Document(autoadd=False)
    document.dummy = 4
    section = Section(autoadd=False)
    section.dummy = 5
    figure = Figure(autoadd=False)
    figure.dummy = 6
    itemize = Itemize(autoadd=False)
    itemize.dummy = 7
    item1 = Item(autoadd=False)
    item1.dummy = 8
    item2 = Item(autoadd=False)
    item2.dummy = 9

    tex.add([documentclass, package])
    document.add(section)
    section.add([figure, itemize])
    itemize.add([item1, item2])

    for 

def test_tree_iter():
    pass

