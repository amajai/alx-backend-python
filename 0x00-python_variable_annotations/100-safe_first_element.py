#!/usr/bin/env python3
"""
safe_first_element module
"""
from typing import Any, Optional


def safe_first_element(lst: list) -> Optional[Any]:
    """
    Return the first element of a list if it exists, otherwise return None.
    """
    if lst:
        return lst[0]
    else:
        return None
