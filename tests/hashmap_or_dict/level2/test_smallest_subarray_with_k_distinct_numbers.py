"""
A file tests the smallest_subarray function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.hashmap_or_dict.level2.smallest_subarray_with_k_distinct_numbers import (
    smallest_subarray,
)


def test_smallest_subarray_example_1():
    """
    Example 1
    Input : arr[] = { 1, 1, 2, 2, 3, 3, 4, 5}
            k = 3
    Output : 5 7
    """
    arr = [1, 1, 2, 2, 3, 3, 4, 5]
    k = 3
    assert smallest_subarray(arr, k) == [5, 7]


def test_smallest_subarray_example_2():
    """
    Example 2
    Input : arr[] = { 1, 2, 2, 3}
            k = 2
    Output : 0 1
    """
    arr = [1, 2, 2, 3]
    k = 2
    assert smallest_subarray(arr, k) == [0, 1]


def test_smallest_subarray_example_3():
    """
    Example 3
    Input : arr[] = {1, 1, 2, 1, 2}
            k = 3
    Output : Invalid k
    """
    arr = [1, 1, 2, 1, 2]
    k = 3
    assert smallest_subarray(arr, k) == "Invalid k"


def test_smallest_subarray_example_4():
    """
    Example 4
    Input : arr[] = {1, 2, 3, 4, 5}
            k = 3
    Output : 0 2
    """
    arr = [1, 2, 3, 4, 5]
    k = 3
    assert smallest_subarray(arr, k) == [0, 2]
