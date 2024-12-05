#!/usr/bin/env python3
"""Type-annotated function make_multiplier that takes a float multiplier as"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by multiplier"""
    def multiplier_function(value: float) -> float:
        """Return the product of value and multiplier"""
        return value * multiplier
    return multiplier_function