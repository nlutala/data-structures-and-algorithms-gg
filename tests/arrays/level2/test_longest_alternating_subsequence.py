"""
A file tests the length_of_longest_subsequence function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.arrays.level2.longest_alternating_subsequence import (
    length_of_longest_subsequence,
)


def test_length_of_longest_subsequence_example_1():
    """
    Example 1:
    Input: arr[] = {1, 5, 4}
    Output: 3
    Explanation: The whole arrays is of the form  x1 < x2 > x3 
    """
    arr = [1, 5, 4]
    assert length_of_longest_subsequence(arr) == 3


def test_length_of_longest_subsequence_example_2():
    """
    Example 2:
    Input: arr[] = {10, 22, 9, 33, 49, 50, 31, 60}
    Output: 6
    Explanation: The subsequences {10, 22, 9, 33, 31, 60} or
    {10, 22, 9, 49, 31, 60} or {10, 22, 9, 50, 31, 60}
    are longest subsequence of length 6
    """
    arr = [10, 22, 9, 33, 49, 50, 31, 60]
    assert length_of_longest_subsequence(arr) == 6
