#!/usr/bin/env python3
"""task 7"""
from typing import Tuple, Union

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Return a tuple where the first element is a string
    and the second is the square of the second argument, cast to float.
    
    Args:
        k (str): The string to be the first element of the tuple.
        v (Union[int, float]): An integer or float whose
                               square will be the second element of the tuple.
        
    Returns:
        Tuple[str, float]: A tuple containing the string
        and the square of the number as a float.
    """
    return (k, float(v ** 2))
