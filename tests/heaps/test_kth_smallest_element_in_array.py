"""
A file tests the find_kth_smallest function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.heaps.kth_smallest_element_in_array import (
    find_kth_smallest,
    find_kth_smallest_no_heap,
)


def test_find_kth_smallest_no_heap_example_1():
    """
    Example 1:
    Input: arr[] = {7, 10, 4, 3, 20, 15}, K = 3
    Output: 7
    """
    arr = [7, 10, 4, 3, 20, 15]
    k = 3
    assert find_kth_smallest(arr, k) == 7


def test_find_kth_smallest_no_heap_example_2():
    """
    Example 2:
    Input: arr[] = {7, 10, 4, 3, 20, 15}, K = 4
    Output: 10
    """
    arr = [7, 10, 4, 3, 20, 15]
    k = 3
    assert find_kth_smallest(arr, k) == 7


def test_find_kth_smallest_example_1():
    """
    Example 1:
    Input: arr[] = {7, 10, 4, 3, 20, 15}, K = 3
    Output: 7
    """
    arr = [7, 10, 4, 3, 20, 15]
    k = 3
    assert find_kth_smallest(arr, k) == 7


def test_find_kth_smallest_example_2():
    """
    Example 2:
    Input: arr[] = {7, 10, 4, 3, 20, 15}, K = 4
    Output: 10
    """
    arr = [7, 10, 4, 3, 20, 15]
    k = 3
    assert find_kth_smallest(arr, k) == 7
