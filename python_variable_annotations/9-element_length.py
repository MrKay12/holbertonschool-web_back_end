#!/usr/bin/env python3
"""Type-annotated function element_length that takes a list of strings"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples, each with a string and its length"""
    return [(i, len(i)) for i in lst]
