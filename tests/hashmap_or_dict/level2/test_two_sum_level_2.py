"""
A file tests the two_sum function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.hashmap_or_dict.level2.two_sum_level_2 import two_sum


def test_two_sum_example_1():
    """
    Example 1
    Input: arr[] = {1, 5, 7, -1, 5}, target= 6
    Output: {{1, 5}, {-1, 7}}
    Explanation: There are only two pairs that add up to 6: {1, 5} and {-1, 7}.
    """
    arr = [1, 5, 7, -1, 5]
    target = 6
    assert two_sum(arr, target) == [[1, 5], [-1, 7]]


def test_two_sum_example_2():
    """
    Example 2
    Input: arr[] = {1, 9, -1, 8, 6}, target = 4
    Output: {{}}
    Explanation: No pairs add up to 4.
    """
    arr = [1, 9, -1, 8, 6]
    target = 4
    assert two_sum(arr, target) == []
