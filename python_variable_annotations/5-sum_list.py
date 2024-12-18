#!/usr/bin/env python3
"""Type-annotated function sum_list that takes a list of floats as argument"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return the sum of the list of floats"""
    return sum(input_list)
