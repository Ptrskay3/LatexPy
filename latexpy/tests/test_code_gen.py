from latexpy.core.code_gen import CodeGen
from latexpy.core.element import *
from latexpy.core.visitors import DefaultChildrenIndentVisitor


def test_codegen_primitive():
    exp = ""
    visitor = DefaultChildrenIndentVisitor()

    def add_p(tree_element):
        nonlocal exp
        exp += tree_element.prefix

    def add_s(tree_element):
        nonlocal exp
        exp += tree_element.suffix

    def add_i(*tree_elements):
        nonlocal exp
        for tree_element in tree_elements:
            if tree_element.accept(visitor):
                exp += tree_element.accept(visitor)

    with Tex() as tex:
        documentclass = Documentclass()
        package = Package()
        with Document() as document:
            with Section() as section:
                figure = Figure()
                with Itemize() as itemize1:
                    item1 = Item()
                    with Itemize() as itemize2:
                        item2 = Item()
                        item3 = Item()
                    item4 = Item()

        add_p(tex)
        add_p(documentclass)
        add_p(package)
        add_p(document)
        add_p(section)
        add_p(figure)
        add_s(figure)
        add_p(itemize1)
        add_i(itemize1)
        add_p(item1)
        add_i(itemize1)
        add_p(itemize2)
        add_i(itemize1, itemize2)
        add_p(item2)
        add_i(itemize1, itemize2)
        add_p(item3)
        add_i(itemize1)
        add_s(itemize2)
        add_i(itemize1)
        add_p(item4)
        add_s(itemize1)
        add_s(document)

        codegen = CodeGen()
        codegen.generate(tex, visitor)
        assert str(codegen) == exp
