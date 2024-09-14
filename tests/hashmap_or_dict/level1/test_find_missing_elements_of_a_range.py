"""
A file tests the missing_elem_in_range function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.hashmap_or_dict.level1.find_missing_elements_of_a_range import (
    missing_elem_in_range,
)


def test_missing_elem_in_range_example_1():
    """
    Example 1
    Input: arr[] = {10, 12, 11, 15}, low = 10, high = 15
    Output: 13, 14
    """
    arr = [10, 12, 11, 15]
    low = 10
    high = 15

    assert missing_elem_in_range(arr, low, high) == [13, 14]


def test_missing_elem_in_range_example_2():
    """
    Example 2
    Input: arr[] = {1, 14, 11, 51, 15}, low = 50, high = 55
    Output: 50, 52, 53, 54, 55
    """
    arr = [1, 14, 11, 51, 15]
    low = 50
    high = 55

    assert missing_elem_in_range(arr, low, high) == [50, 52, 53, 54, 55]
