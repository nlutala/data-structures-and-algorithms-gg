"""
A file tests the two_sum_exists function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.arrays.level2.pair_with_given_sum import two_sum_exists


def test_two_sum_exists_example_1():
    """
    Example 1:
    Input: arr[] = {0, -1, 2, -3, 1}, target = -2
    Output: True
    Explanation: If we calculate the sum of the output,1 + (-3) = -2
    """
    arr = [0, -1, 2, -3, 1]
    target = -2
    assert two_sum_exists(arr, target) == True


def test_two_sum_exists_example_2():
    """
    Example 2:
    Input: arr[] = {1, -2, 1, 0, 5}, target = 0
    Output: False
    """
    arr = [1, -2, 1, 0, 5]
    target = 0
    assert two_sum_exists(arr, target) == False
