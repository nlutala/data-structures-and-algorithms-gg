"""
A file tests the count_equal_num_of_1_and_0 function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.arrays.level2.count_subarrays_with_equal_num_of_1_and_0 import (
    count_equal_num_of_1_and_0,
)


def test_count_equal_num_of_1_and_0_example_1():
    """
    Example 1:
    Input: arr[] = {1, 0, 0, 1, 0, 1, 1}
    Output: 8
    Explanation: The index range for the 8 sub-arrays are:
    (0, 1), (2, 3), (0, 3), (3, 4), (4, 5), (2, 5), (0, 5), (1, 6)
    """
    arr = [1, 0, 0, 1, 0, 1, 1]

    assert count_equal_num_of_1_and_0(arr) == 8


def test_count_equal_num_of_1_and_0_example_2():
    """
    Example 2:
    Input: arr = {1, 0, 0, 1, 1, 0, 0, 1}
    Output: 12
    """
    arr = [1, 0, 0, 1, 1, 0, 0, 1]

    assert count_equal_num_of_1_and_0(arr) == 12
