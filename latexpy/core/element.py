from typing import Union, Callable

from latexpy.core.base import AbstractElement
from latexpy.util.decorator import require_type

class Tex(AbstractElement):
    """
    """
    def __init__(self):
        super().__init__()


    @require_type(1, AbstractElement)
    def _add(self, child: AbstractElement) -> None:
        pass

    def __iter__(self):
        return self


class CallableElement(Tex):

    _name = ''
    
    def __init__(self):
        super().__init__()

    @property
    def name(self):
        return self._name

class Environment(CallableElement):
    def __init__(self):
        super().__init__()

class Function(CallableElement):
    def __init__(self):
        super().__init__()


class Package(Function):
    _name = 'usepackage'






class PlainText(Tex):
    def __init__(self):
        super().__init__()

p = Package()

print(p.name)