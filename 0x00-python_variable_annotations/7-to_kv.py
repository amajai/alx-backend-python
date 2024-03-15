#!/usr/bin/env python3
"""
to_kv module
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    takes a float n as argument and returns
    the string representation of the float.
    """
    return (k, v**2)
