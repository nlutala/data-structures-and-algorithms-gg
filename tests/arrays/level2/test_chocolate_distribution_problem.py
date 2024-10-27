"""
A file tests the distribute_chocolate function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.arrays.level2.chocolate_distribution_problem import (
    distribute_chocolate,
)


def test_distribute_chocolate_example_1():
    """
    Example 1:
    Input: arr[] = {7, 3, 2, 4, 9, 12, 56}, m = 3
    Output: 2
    Explanation: If we distribute chocolate packets {3, 2, 4}, we will get the
    minimum difference, that is 2.
    """
    arr = [7, 3, 2, 4, 9, 12, 56]
    m = 3
    assert distribute_chocolate(arr, m) == 2


def test_distribute_chocolate_example_2():
    """
    Example 2:
    Input: arr[] = {7, 3, 2, 4, 9, 12, 56}, m = 5
    Output: 7
    Explanation: If we distribute chocolate packets {3, 2, 4, 9, 7}, we will
    get the minimum difference, that is 9 – 2 = 7.
    """
    arr = [7, 3, 2, 4, 9, 12, 56]
    m = 5
    assert distribute_chocolate(arr, m) == 7
