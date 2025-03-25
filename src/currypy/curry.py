from functools import partial, wraps
from inspect import signature, getcallargs, getfullargspec
from typing import Callable


def curry(f: Callable):
    """
    Creates a new and curryable function from a Callable.
    """

    def count_args(f: partial, *args, **kwargs):
        # print(signature(f))
        
        match isinstance(f, partial):
            case True:
                # print(f"args: {f.args}, kwargs: {f.keywords}")

                return len(f.args) + len(f.keywords)
            case False:
                # print(f"args: {args}, kwargs: {kwargs}") 

                return len(args) + len(kwargs)
    
    def examine(f: Callable, *args, **kwargs):
        part = partial(f, *args, **kwargs)
        spec = getfullargspec(part)

        print(f"args: {spec.args}")
        print(f"kwonlyargs: {spec.kwonlyargs}")
        print(f"kwonlydefaults: {spec.kwonlydefaults}")
        print(f"signature: {signature(partial(f, *args, **kwargs))}")
    
    def check_args(f: Callable, *args, **kwargs):
        part = partial(f, *args, **kwargs)
        spec = getfullargspec(part)

        examine(f, *args, **kwargs)

        # check = True if len(spec.args) == 0 and (len(spec.kwonlyargs) == len(spec.kwonlydefaults)) else False

        match spec.kwonlydefaults:
            case None:
                check = True if len(spec.args) == 0 else False
            case _:
                check = True if len(spec.args) == 0 and len(spec.kwonlyargs) == len(spec.kwonlydefaults) else False
        
        match len(spec.args) == 0:
            case True:
                match len(spec.kwonlyargs) == len(spec.kwonlydefaults):
                    case True:
                        return partial(f, *args, **kwargs)

        print(check)
        print('==============')

        return check

    # @wraps(f)
    def wrapper(*args, **kwargs):
        # if check_args(f, *args, **kwargs) == True:
        #     match getfullargspec(partial(f, *args, **kwargs)).kwonlydefaults:
        #         case None:
        #             return f(*args, **kwargs)
        #         case _:
        #             return partial(f, *args, **kwargs)

        # spec = getfullargspec(partial(f, *args, **kwargs))

        # match spec.defaults:
        #     case None:
        #         match len(spec.args) == 0:
        #             case True:
        #                 return f(*args, **kwargs)

        def apply_defaults(f: Callable, *args, **kwargs):
            params = signature(f).parameters


        return curry(partial(f, *args, **kwargs))

    return wrapper
