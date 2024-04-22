#!/usr/bin/env python3
"""callable methode"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a function that multiplies any given
    float by a predefined multiplier.

    Args:
        multiplier (float): The multiplier to use in the returned function.

    Returns:
        Callable[[float], float]: A function that takes a float
        and returns it multiplied by the multiplier.
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier
    return multiplier_function
