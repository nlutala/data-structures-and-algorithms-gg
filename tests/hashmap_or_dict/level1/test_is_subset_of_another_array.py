"""
A file tests the is_subset function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.hashmap_or_dict.level1.is_subset_of_another_array import (
    is_subset
)


def test_is_subset_example_1():
    """
    Example 1:
    Input: arr1[] = {11, 1, 13, 21, 3, 7}, arr2[] = {11, 3, 7, 1}
    Output: True
    """
    arr1 = [11, 1, 13, 21, 3, 7]
    arr2 = [11, 3, 7, 1]

    assert is_subset(arr1, arr2) is True


def test_is_subset_example_2():
    """
    Example 2:
    Input: arr1[] = {1, 2, 3, 4, 5, 6}, arr2[] = {1, 2, 4}
    Output: True
    """
    arr1 = [1, 2, 3, 4, 5, 6]
    arr2 = [1, 2, 4]

    assert is_subset(arr1, arr2) is True


def test_is_subset_example_3():
    """
    Example 3:
    Input: arr1[] = {10, 5, 2, 23, 19}, arr2[] = {19, 5, 3}
    Output: False
    """
    arr1 = [10, 5, 2, 23, 19]
    arr2 = [19, 5, 3]

    assert is_subset(arr1, arr2) is False
