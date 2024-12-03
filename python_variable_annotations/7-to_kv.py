#!/usr/bin/env python3
"""Type-annotated function that takes a string and
    an int OR float as arguments and returns tuple"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with k and the square of v"""
    return (k, float(v ** 2))
