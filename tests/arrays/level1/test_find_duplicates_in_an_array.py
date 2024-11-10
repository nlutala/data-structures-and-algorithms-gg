"""
A file test the get_duplicates function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.arrays.level1.find_duplicates_in_an_array import (
    get_duplicates,
)


def test_get_duplicates_example_1() -> None:
    """
    Example 1:
    Input: {2, 10, 10, 100, 2, 10, 11, 2, 11, 2}
    Output: {2, 10, 11}
    """
    arr = [2, 10, 10, 100, 2, 10, 11, 2, 11, 2]
    assert get_duplicates(arr) == [2, 10, 11]


def test_get_duplicates_example_2() -> None:
    """
    Example 2:
    Input: {5, 40, 1, 40, 100000, 1, 5, 1}
    Output: {5, 40, 1}
    """
    arr = [5, 40, 1, 40, 100000, 1, 5, 1]
    assert get_duplicates(arr) == [5, 40, 1]
