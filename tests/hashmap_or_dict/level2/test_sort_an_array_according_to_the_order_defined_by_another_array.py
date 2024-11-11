"""
A file tests the sort_array function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.hashmap_or_dict.level2.sort_an_array_according_to_the_order_defined_by_another_array import (
    sort_array,
)


def test_sort_array_example_1():
    """
    Example 1
    Input: arr1[] = {2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8}
           arr2[] = {2, 1, 8, 3}
    Output: arr1[] = {2, 2, 1, 1, 8, 8, 3, 5, 6, 7, 9}
    """
    arr1 = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]
    arr2 = [2, 1, 8, 3]
    assert sort_array(arr1, arr2) == [2, 2, 1, 1, 8, 8, 3, 5, 6, 7, 9]


def test_sort_array_example_2():
    """
    Example 2
    Input: arr1[] = {4, 5, 1, 1, 3, 2}
           arr2[] = {3, 1}
    Output: arr1[] = {3, 1, 1, 2, 4, 5}
    """
    arr1 = [4, 5, 1, 1, 3, 2]
    arr2 = [3, 1]
    assert sort_array(arr1, arr2) == [3, 1, 1, 2, 4, 5]
