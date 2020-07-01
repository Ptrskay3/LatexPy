from typing import Union, Callable

from latexpy.core.base import AbstractElement
from latexpy.util.decorator import require_type

class Tex(AbstractElement):
    """
    """
    def __init__(self):
        super().__init__()


    @require_type('child', AbstractElement)
    def _add(self, child: AbstractElement) -> None:
        pass

    def __iter__(self):
        return self

class CallableElement(Tex):
    def __init__(self):
        super().__init__()

class Function(CallableElement):
    pass


class Environment(CallableElement):
    pass

class PlainText(Tex):
    def __init__(self):
        super().__init__()

t = CallableElement()
a = Environment()
g = 63
p = PlainText()
# print(type(t), type(p))
t._add(child=p)