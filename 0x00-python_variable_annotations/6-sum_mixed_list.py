#!/usr/bin/env python3
"""
This module provides a function to sum a list of integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sum a list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): List of integers and float numbers.

    Returns:
        float: The sum of the numbers.
    """
    return sum(mxd_lst)
