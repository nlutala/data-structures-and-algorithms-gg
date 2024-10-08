"""
A file tests the count_sum_pairs function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.hashmap_or_dict.level1.count_all_distinct_pairs import (
    count_sum_pairs,
)


def test_count_sum_pairs_example_1():
    """
    Example 1
    Input: arr[] = {1, 5, 3, 4, 2}, k = 3
    Output: 2
    Explanation: There are 2 pairs with difference 3, the pairs are {1, 4} and
    {5, 2}
    """
    arr = [1, 5, 3, 4, 2]
    k = 3
    assert count_sum_pairs(arr, k) == 2


def test_count_sum_pairs_example_2():
    """
    Example 2
    Input: arr[] = {8, 12, 16, 4, 0, 20}, k = 4
    Output: 5
    There are 5 pairs with difference 4, the pairs are {0, 4}, {4, 8}, {8, 12},
    {12, 16} and {16, 20}
    """
    arr = [8, 12, 16, 4, 0, 20]
    k = 4
    assert count_sum_pairs(arr, k) == 5
