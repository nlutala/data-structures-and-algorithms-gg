"""
A file tests the three_sum function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.arrays.level2.find_triplet_that_sums_to_given_value import (
    three_sum,
)


def test_three_sum_example_1():
    """
    Example 1:
    Input: arr = {12, 3, 4, 1, 6, 9}, sum = 24;
    Output: 12, 3, 9
    Explanation: There is a triplet (12, 3 and 9) present in the array whose
    sum is 24.
    """
    arr = [12, 3, 4, 1, 6, 9]
    sum = 24
    assert three_sum(arr, sum) == sorted([12, 3, 9])


def test_three_sum_example_2():
    """
    Example 2:
    Input: arr = {1, 2, 3, 4, 5}, sum = 9
    Output: 5, 3, 1
    Explanation: There is a triplet (5, 3 and 1) present in the array whose
    sum is 9.
    """
    arr = [1, 2, 3, 4, 5]
    sum = 9
    assert three_sum(arr, sum) == sorted([5, 3, 1])


def test_three_sum_example_3():
    """
    Example 3:
    Input: arr = {2, 10, 12, 4, 8}, sum = 9
    Output: No Triplet
    Explanation: We do not print in this case and return false.
    """
    arr = [2, 10, 12, 4, 8]
    sum = 9
    assert three_sum(arr, sum) is None


# Custom tests
def test_three_sum_example_4():
    """
    Example 3:
    Input: arr = {1, 1, 3, 4, 8}, sum = 5
    Output: [1, 1, 3]
    """
    arr = [1, 1, 3, 4, 8]
    sum = 5
    assert three_sum(arr, sum) == [1, 1, 3]
