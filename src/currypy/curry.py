from functools import partial, reduce
from inspect import BoundArguments, signature, getargs
from typing import Callable


def curry(f: Callable | partial):
    """
    Creates a new and curryable function from a Callable.
    """
    
    def count_args(f: partial):
        return reduce(lambda a, c: a + len(c), (f.args, f.keywords), 0)

    def apply_defaults(f: partial):
        def filter_args(f: partial):
            return filter(lambda x: x != ..., f.args)

        def bind_args(f: partial):
            return signature(f.func).bind_partial(*filter_args(f), **f.keywords)
        
        def partial_with_defaults(f: partial, ba: BoundArguments):
            return ba.apply_defaults() or partial(f.func, *ba.args, **ba.kwargs)

        return partial_with_defaults(f, bind_args(f))

    def wrapper(*args, **kwargs):
        def is_base_case(f: partial):
            return len(getargs(f.func.__code__)) == count_args(f)
        
        def select_default_args(f: partial, *args):
            return apply_defaults(f) if ... in args else f

        def case_result(f: partial):        
            match is_base_case(f):
                case True:
                    return f()
                case False:
                    return curry(f)
        
        return case_result(select_default_args(partial(f, *args, **kwargs), *args))

    return wrapper
