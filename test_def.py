from arg_types import *
from foo import Foo
import numpy as np


def inproduct(v: Vector_t, arg2: str) -> V_Foo_t:
    ret = sum(x * y for x, y in v)
    return [Foo(ret)]


def builtins_only(arg2: float, arg3: int ) -> complex:
    return complex(arg2,arg3)

def max_np_array(arg1: NpArr_t) -> float:
    return arg1.max()


def void_method(arg: str):
    pass

def void_no_args():
    pass

def starargs(*args):
    pass

def starkwargs(**kwargs):
    pass


