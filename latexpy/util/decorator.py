from inspect import getfullargspec
from typing import Union, Callable, Any

__all__ = ['require_type']

def require_type(arg: Union[int, str], *types) -> Callable:
    def wrapper(f: Callable) -> Callable:
        def new_f(*args, **kwargs) -> Any:
            val = get_param(f, arg, *args, **kwargs)
            if not any(isinstance(val, type_) for type_ in types):
                raise TypeError("Types don't match.")
            return f(*args, **kwargs)
        new_f.__name__ = f.__name__
        return new_f
    return wrapper

def get_param(f, arg: Union[int, str], *args, **kwargs) -> Any:
    spec = getfullargspec(f)
    N = len(args) - 1
    if isinstance(arg, int):
        if N >= arg:
            return args[arg]
        else:
            try:
                return kwargs.get(spec.args[arg])
            except IndexError:
                raise IndexError('Argument number out of range.')
    elif isinstance(arg, str):
        return kwargs.get(arg)
    else:
        raise TypeError('Expected `int` or `str` type for arg.')
