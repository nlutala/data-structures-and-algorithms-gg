"""
A file tests the count_pairs_with_sum function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.arrays.level2.count_pairs_with_given_sum import (
    count_pairs_with_sum,
)


def test_count_pairs_with_sum_example_1():
    """
    Example 1:
    Input: arr[] = {1, 5, 7, -1}, K = 6
    Output:  2
    Explanation: Pairs with sum 6 are (1, 5) and (7, -1).
    """
    arr = [1, 5, 7, -1]
    k = 6

    assert count_pairs_with_sum(arr, k) == 2


def test_count_pairs_with_sum_example_2():
    """
    Example 2:
    Input: arr[] = {1, 5, 7, -1, 5}, K = 6
    Output:  3
    Explanation: Pairs with sum 6 are (1, 5), (7, -1) & (1, 5).
    """
    arr = [1, 5, 7, -1, 5]
    k = 6

    assert count_pairs_with_sum(arr, k) == 3
