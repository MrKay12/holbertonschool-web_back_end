#!/usr/bin/env python3
"""Type-annotated function that takes a list of
    integers and floats argument and returns sum as float"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of the list of integers and floats"""
    return sum(mxd_lst)
