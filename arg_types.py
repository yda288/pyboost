from typing import TypeVar, Type, List, Tuple, Dict
from foo import Foo
import numpy as np

Vector_t = List[Tuple[float, float]]
V_Foo_t = List[Type[Foo]]
Map_t = Dict[str, float]
NpArr_t = Type[np.ndarray[float]]