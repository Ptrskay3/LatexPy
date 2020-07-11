from latexpy.core.element import Tex
from latexpy.core.visitors import DefaultChildrenIndentVisitor


class CodeGen(object):
    def __init__(self):
        self.code = ""
        self.global_prefix = ""
        self.global_suffix = ""

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, val):
        self._code = val

    def generate(
        self,
        tex_tree: Tex,
        indent_visitor: DefaultChildrenIndentVisitor = DefaultChildrenIndentVisitor(),
    ):
        self.code += self.global_prefix
        self.code += tex_tree.prefix
        children_prefix = tex_tree.accept(indent_visitor)
        if children_prefix:
            self.global_prefix += children_prefix
        for child in tex_tree.children:
            self.generate(child, indent_visitor)
        if children_prefix:
            self.global_prefix = self.global_prefix[: -len(children_prefix)]
            self.code += self.global_prefix
        self.code += tex_tree.suffix
        self.code += self.global_suffix

    def __str__(self):
        return self.code
