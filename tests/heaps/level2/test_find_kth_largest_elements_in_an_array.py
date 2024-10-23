"""
A file tests the k_largest_elements function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.heaps.level2.find_kth_largest_elements_in_an_array import (
    k_largest_elements,
)


def test_find_kth_largest_elements_example_1():
    """
    Example 1:
    Input: [1, 23, 12, 9, 30, 2, 50], K = 3
    Output: 50, 30, 23
    """
    arr, k = [1, 23, 12, 9, 30, 2, 50], 3
    assert k_largest_elements(arr, k) == [50, 30, 23]


def test_find_kth_largest_elements_example_2():
    """
    Input:  [11, 5, 12, 9, 44, 17, 2], K = 2
    Output: 44, 17
    """
    arr, k = [11, 5, 12, 9, 44, 17, 2], 2
    assert k_largest_elements(arr, k) == [44, 17]
