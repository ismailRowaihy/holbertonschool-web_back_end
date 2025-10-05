#!/usr/bin/env python3
"""
the module is a function that takes a list of float and returns a float
"""
import typing


def to_kv(k: str , v : typing.Union[int,float]) -> typing.Tuple[str, float]:
    """
    this fucntion takes a list of float retruns its sum as a float
    """
    return (k,float(v**2))
