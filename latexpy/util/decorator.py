from typing import Union, Callable, Any

__all__ = ['require_type']

def require_type(arg: Union[int, str], *types) -> Callable:
    def wrapper(f: Callable) -> Callable:
        def new_f(*args, **kwargs) -> Any:
            val = get_param(arg, *args, **kwargs)
            if not any(isinstance(val, type_) for type_ in types):
                raise TypeError("Types don't match.")
            return f(*args, **kwargs)
        new_f.__name__ = f.__name__
        return new_f
    return wrapper

def get_param(arg: Union[int, str], *args, **kwargs) -> Any:
    if isinstance(arg, int):
        try:
            return args[arg]
        except IndexError:
            return kwargs.get(arg, None)
    elif isinstance(arg, str):
        return kwargs.get(arg, None)
    else:
        raise ValueError