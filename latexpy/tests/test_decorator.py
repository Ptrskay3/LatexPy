import pytest
from latexpy.util.decorator import require_type

def test_require_type_1():
    
    @require_type(1, int)
    def func(x, y):
        return None

    with pytest.raises(TypeError):
        func('a', 'a')

def test_require_type_2():

    @require_type(84, int)
    def func(x, y):
        return None

    with pytest.raises(IndexError):
        func('a', 'a')

def test_require_type_3():
    
    @require_type(1, int)
    def func(x, y):
        return None

    func(x='a', y=1)

def test_require_type_4():
    
    @require_type(1, int)
    def func(x, y):
        return None

    func(y=1, x='a')


def test_require_type_5():
    
    @require_type(2, float)
    def func(x, y, *args, **kwargs):
        return x

    func(1, 'a', 4E-10)

def test_require_type_6():
    
    @require_type(1, float)
    def func():
        return

    with pytest.raises(IndexError):
        func()

def test_require_type_7():
    
    @require_type(4.5, float)
    def func(x, y):
        return

    with pytest.raises(TypeError):
        func(1, 2)

def test_require_type_8():
    
    @require_type('x', int)
    def func(x, y, z):
        return

    func(x=1, y=4, z=6)


# -------------------------------------
# def test_require_type_7():
    
#     @require_type(2, float)
#     def func(x, y, *args, **kwargs):
#         return x

#     func(x=1, y='a', c=4E-10)

# -------------------------------------

# def test_require_type_8():
    
#     @require_type('x', int)
#     def func(x, y, z):
#         return

#
#     func(1, 4, 6)
# -------------------------------------