"""
A file tests the quick_sort function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.arrays.level2.quick_sort_algorithm import quick_sort


def test_quick_sort_example_1():
    """
    Example 1:
    Input: arr[] = {10, 80, 30, 90, 40, 50, 70}
    Output: arr[] = {10, 30, 40, 50, 70, 80, 90}
    """
    arr = [10, 80, 30, 90, 40, 50, 70]

    assert quick_sort(arr) == sorted([10, 80, 30, 90, 40, 50, 70])


def test_quick_sort_example_2():
    """
    Example 2:
    Input: arr[] = {10, 80, 30, 90, 40}
    Output: arr[] = {10, 30, 40, 80, 90}
    """
    arr = [10, 80, 30, 90, 40]

    assert quick_sort(arr) == sorted([10, 80, 30, 90, 40])
