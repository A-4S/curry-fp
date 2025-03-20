from functools import partial, wraps
from inspect import signature
from typing import Callable


def curry(f: Callable):
    """
    Creates a new and curryable function from a Callable.
    """

    def count_args(f: partial, *args, **kwargs):
        return len(f.args) if isinstance(f, partial) else len(args) + len(kwargs)

    @wraps(f)
    def wrapper(*args, **kwargs):
        if count_args(f, *args, **kwargs) >= len(signature(f).parameters):
            return f(*args, **kwargs)

        return curry(partial(f, *args, **kwargs))

    return wrapper
