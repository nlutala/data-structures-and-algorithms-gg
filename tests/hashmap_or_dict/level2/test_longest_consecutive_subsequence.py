"""
A file tests the consecutive_subsequence function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.hashmap_or_dict.level2.longest_consecutive_subsequence import (
    consecutive_subsequence_len,
)


def test_consecutive_subsequence_len_example_1():
    """
    Example 1
    Input: arr[] = {1, 9, 3, 10, 4, 20, 2}
    Output: 4
    Explanation: The subsequence 1, 3, 4, 2 is the longest subsequence of consecutive
    elements
    """
    arr = [1, 9, 3, 10, 4, 20, 2]
    assert consecutive_subsequence_len(arr) == 4


def test_consecutive_subsequence_len_example_2():
    """
    Example 2
    Input: arr[] = {36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42}
    Output: 5
    Explanation: The subsequence 36, 35, 33, 34, 32 is the longest subsequence of
    consecutive elements.
    """
    arr = [36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42]
    assert consecutive_subsequence_len(arr) == 5
