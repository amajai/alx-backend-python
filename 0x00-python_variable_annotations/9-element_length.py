#!/usr/bin/env python3
"""
element_length module
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    element_length function return elements length
    """
    return [(i, len(i)) for i in lst]
