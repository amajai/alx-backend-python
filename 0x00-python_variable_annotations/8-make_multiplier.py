#!/usr/bin/env python3
"""
make_multiplier module
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    takes a float n as argument and returns
    the string representation of the float.
    """
    def f(m):
        return m**2
    return f
