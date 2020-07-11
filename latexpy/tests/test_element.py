import pytest

from latexpy.core.element import *
from latexpy.util.string import diff


@pytest.fixture()
def elements():
    f = Tex()
    g = Tex()
    h = CallableElement(autoadd=False)
    j = CallableElement(autoadd=False)
    k = CallableElement(autoadd=False)
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
    expected = list(range(1, 10))
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

        res = [a.dummy for a in tex]
        assert expected == res


def test_tree_construction_flat():
    expected = list(range(1, 10))
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

    tex.add([documentclass, package, document])
    document.add(section)
    section.add([figure, itemize])
    itemize.add([item1, item2])

    assert expected == [a.dummy for a in tex]


def test_tree_iter():
    pass


def test_tex_iter():
    class Dummy(Tex):
        def __init__(self, num):
            super().__init__()
            self.num = num

        def __str__(self):
            return str(self.num)

    tex = Dummy(1)
    documentclass = Dummy(2)
    package = Dummy(3)
    tex.add([documentclass, package])

    assert [1, 2, 3] == [t.num for t in tex]

def test_latexcode():
    content=r"\begin{enumerate}\item a \item $<|ß@&#|>$"
    latexcode=LatexCode(content,autoadd=False)
    assert latexcode.prefix == content
    assert latexcode.suffix == ""

def test_plaintext():
    cnt=r"\begin{enumerate}\item a \item $<|@&#|>$"
    expected = r"\textbackslash begin\{enumerate\}\textbackslash item a \textbackslash item \$\textless \textbar @\&\#\textbar \textgreater \$"
    plaintext=PlainText(cnt,autoadd=False)
    # print(plaintext.content)
    # assert plaintext.prefix == expected
    # assert plaintext.suffix == ""
    diff(expected, plaintext.prefix)

test_plaintext()