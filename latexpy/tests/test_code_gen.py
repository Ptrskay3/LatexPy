import pytest
from latexpy.core.element import *
from latexpy.core.code_gen import CodeGen

def test_codegen_primitive():
    with Tex() as tex:
        Documentclass()
        Package()
        with Document():
            with Section():
                Figure()
                with Itemize():
                    Item()
                    with Itemize():
                        Item()
                        Item()
                    Item()

        codegen = CodeGen()
        codegen.generate(tex)
