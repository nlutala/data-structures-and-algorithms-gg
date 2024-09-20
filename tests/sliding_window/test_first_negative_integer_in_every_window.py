"""
A file tests the find_first_negative_ints function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.sliding_window.first_negative_integer_in_every_window import (
    find_first_negative_ints,
)


def test_find_first_negative_ints_example_1() -> None:
    """
    Example 1
    Input : arr[] = {-8, 2, 3, -6, 10}, k = 2
    Output : -8 0 -6 -6
    First negative integer for each window of size k
    {-8, 2} = -8
    {2, 3} = 0 (does not contain a negative integer)
    {3, -6} = -6
    {-6, 10} = -6
    """
    arr = [-8, 2, 3, -6, 10]
    k = 2
    assert find_first_negative_ints(arr, k) == [-8, 0, -6, -6]


def test_find_first_negative_ints_example_2() -> None:
    """
    Example 2
    Input : arr[] = {12, -1, -7, 8, -15, 30, 16, 28} , k = 3
    Output : -1 -1 -7 -15 -15 0
    """
    arr = [12, -1, -7, 8, -15, 30, 16, 28]
    k = 3
    assert find_first_negative_ints(arr, k) == [-1, -1, -7, -15, -15, 0]
