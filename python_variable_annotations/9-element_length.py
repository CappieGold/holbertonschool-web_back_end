#!/usr/bin/env python3
"""task 9"""

from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples, each containing a sequence and its length.

    Args:
        lst (Iterable[Sequence]): An iterable collection of
                                  sequences (like lists or strings).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples,
        where each tuple contains a sequence and the length of that sequence.
    """
    return [(i, len(i)) for i in lst]
