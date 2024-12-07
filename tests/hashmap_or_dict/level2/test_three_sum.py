"""
A file tests the get_three_sum function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.hashmap_or_dict.level2.three_sum import get_three_sum


def test_get_three_sum_example_1():
    """
    Example 1
    Input: arr[] = [12, 3, 6, 1, 6, 9], target = 24
    Output: [[3, 9, 12], [6, 6, 12]]
    Explanation: There are two unique triplets that add up to 24:
    3 + 9 + 12 = 24
    6 + 6 + 12 = 24
    """
    arr = [12, 3, 6, 1, 6, 9]
    target = 24
    assert get_three_sum(arr, target) == [[3, 9, 12], [6, 6, 12]]


def test_get_three_sum_example_2():
    """
    Example 2
    Input: arr[] = {-2, 0, 1, 1, 2}, target = 10
    Output: {}
    Explanation: There is not triplet with sum 10.
    """
    arr = [-2, 0, 1, 1, 2]
    target = 10
    assert get_three_sum(arr, target) == []
