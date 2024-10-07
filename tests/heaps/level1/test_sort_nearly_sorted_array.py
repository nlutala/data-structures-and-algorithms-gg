"""
A file that tests the sort_array functions

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.heaps.level1.sort_nearly_sorted_array import sort_array


def test_sort_array_example_1():
    """
    Example 1:
    Input: arr[] = {6, 5, 3, 2, 8, 10, 9}, K = 3
    Output: arr[] = {2, 3, 5, 6, 8, 9, 10}
    """
    arr = [6, 5, 3, 2, 8, 10, 9]
    k = 3
    assert sort_array(arr, k) == [2, 3, 5, 6, 8, 9, 10]


def test_sort_array_example_2():
    """
    Example 2:
    Input: arr[] = {10, 9, 8, 7, 4, 70, 60, 50}, k = 4
    Output: arr[] = {4, 7, 8, 9, 10, 50, 60, 70}
    """
    arr = [10, 9, 8, 7, 4, 70, 60, 50]
    k = 4
    assert sort_array(arr, k) == [4, 7, 8, 9, 10, 50, 60, 70]


def test_sort_array_example_3():
    """
    Example 3: (My own test)
    Input: arr[] = {33, 10, 8, 54, 3, 1, 60, 50}, k = 4
    Output: arr[] = {1, 3, 8, 10, 33, 50, 54, 60}
    """
    arr = [33, 10, 8, 54, 3, 1, 60, 50]
    k = 4
    assert sort_array(arr, k) == [1, 3, 8, 10, 33, 50, 54, 60]
