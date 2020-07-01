import abc

class LatexElementMeta(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def method(self):
        pass

class LatexElements(LatexElementMeta):
    def __init__(self):
        self._elements = set()

    def method(self):
        for el in self._elements:
            el.method()

    def add(self, element):
        self._elements.add(element)

    def remove(self, element):
        self._elements.discard(element)


class FinalElement(LatexElementMeta):

    def method(self):
        pass