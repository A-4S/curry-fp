from functools import partial, reduce
from inspect import signature, getargs
from typing import Callable


def curry(f: Callable | partial):
    """
    Creates a new and curryable function from a Callable.
    """
    
    def count_args(f: Callable | partial, *args, **kwargs):
        def count_items(*args):
            return reduce(lambda a, c: a + len(c), args, 0)

        return count_items(f.args, f.keywords) if hasattr(f, 'args') else count_items(args, kwargs)
    
    def apply_defaults(f: partial):
        def filter_args(f: partial):
            return filter(lambda x: x != ..., f.args)

        sig = signature(f.func)
        ba = sig.bind_partial(*filter_args(f), **f.keywords)

        return ba.apply_defaults() or partial(f.func, *ba.args, **ba.kwargs)

    def wrapper(*args, **kwargs):
        def is_base_case(f: partial, *args, **kwargs):
            return len(getargs(f.func.__code__)) == count_args(f, *args, **kwargs)
        
        f_a = partial(f, *args, **kwargs)
        f_b = apply_defaults(f_a) if ... in args else f_a
        
        match is_base_case(f_b, *args, **kwargs):
            case True:
                return f_b()
            case False:
                return curry(f_b)

    return wrapper
