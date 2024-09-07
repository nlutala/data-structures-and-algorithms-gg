"""
A file tests the find_subarray_with_0_sum function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.arrays.level2.max_subarray_sum import get_max_subarray_sum


def test_get_max_subarray_sum_example_1():
    """
    Example 1:
    Input: {-2,-3,4,-1,-2,1,5,-3}
    Output: 7
    Explanation: sum(4,-1,-2,1,5) is 7, which is the greatest sum.
    """
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]

    assert get_max_subarray_sum(arr) == 7


def test_get_max_subarray_sum_example_2():
    """
    Example 2:
    Input: {2}
    Output: 2
    """
    arr = [2]

    assert get_max_subarray_sum(arr) == 2


def test_get_max_subarray_sum_example_3():
    """
    Example 3:
    Input: {5,4,1,7,8}
    Output: 25
    """
    arr = [5, 4, 1, 7, 8]

    assert get_max_subarray_sum(arr) == 25
