from functools import partial, wraps
from inspect import signature
from typing import Callable


def curry(f: Callable):
    """
    Creates a new and curryable function from a Callable.
    """

    def partial_signature_arguments(*args, **kwargs):
        return signature(f).bind_partial(*args, **kwargs).arguments

    @wraps(f)
    def wrapper(*args, **kwargs):
        if len(partial_signature_arguments(*args, **kwargs)) >= len(signature(f).parameters):
            return f(*args, **kwargs)

        return curry(wraps(f)(partial(f, *args, **kwargs)))

    return setattr(wrapper, "__signature__", signature(f)) or wrapper
