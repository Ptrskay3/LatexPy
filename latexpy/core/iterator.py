from collections.abc import Iterator

from latexpy.core.base import AbstractElement

class PreorderIterator(Iterator):
    def __init__(self, element: AbstractElement):
        super().__init__()
        self.element = element

    def __iter__(self):
        yield self.element
        for child in self.element.children:
            yield from PreorderIterator(child)

    # FIX
    def __next__(self):
        pass


class PostorderIterator(Iterator):
    def __init__(self, element: AbstractElement):
        super().__init__()
        self.element = element

    def __iter__(self):
        for child in list(self.element.children)[::-1]:
            yield from PostorderIterator(child)
        yield self.element

    # FIX
    def __next__(self):
        pass
