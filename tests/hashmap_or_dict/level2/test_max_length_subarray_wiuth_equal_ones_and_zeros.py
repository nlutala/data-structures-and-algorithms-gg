"""
A file tests the range_of_equal_1s_and_0s function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.hashmap_or_dict.level2.max_length_subarray_with_equal_ones_and_zeros import (
    range_of_equal_1s_and_0s,
)


def test_range_of_equal_1s_and_0s_example_1():
    """
    Example 1
    Input: arr[] = {1, 0, 1, 1, 1, 0, 0}
    Output: 1 to 6 (Starting and Ending indexes of output subarray)
    """
    arr = [1, 0, 1, 1, 1, 0, 0]
    assert range_of_equal_1s_and_0s(arr) == "1 to 6"


def test_range_of_equal_1s_and_0s_example_2():
    """
    Example 2
    Input: arr[] = {1, 1, 1, 1}
    Output: No such subarray
    """
    arr = [1, 1, 1, 1]
    assert range_of_equal_1s_and_0s(arr) == "No such subarray"


def test_range_of_equal_1s_and_0s_example_3():
    """
    Example 3
    Input: arr[] = {0, 0, 1, 1, 0}
    Output: 0 to 3 Or 1 to 4
    """
    arr = [0, 0, 1, 1, 0]
    assert range_of_equal_1s_and_0s(arr) == "0 to 3"
