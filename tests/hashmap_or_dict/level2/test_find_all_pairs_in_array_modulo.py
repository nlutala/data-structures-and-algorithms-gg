"""
A file tests the find_pairs_a_modulo_b function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.hashmap_or_dict.level2.find_all_pairs_in_array_modulo import (
    find_pairs_a_modulo_b,
)


def test_find_pairs_a_modulo_b_example_1():
    """
    Example 1
    Input: arr[] = {2, 3, 5, 4, 7}, k = 3
    Output: (3, 5), (3, 4), (3, 7), (7, 4)
    7 % 4 = 3
    3 % 4 = 3
    3 % 5 = 3
    3 % 7 = 3
    """
    arr, k = [2, 3, 5, 4, 7], 3
    assert find_pairs_a_modulo_b(arr, k) == [(3, 5), (3, 4), (3, 7), (7, 4)]


def test_find_pairs_a_modulo_b_example_2():
    """
    Example 2
    Input: arr[] = [1, 2], k = 3
    Output: 0
    Explanation: No pairs give remainder 3.
    """
    arr, k = [1, 2], 3
    assert find_pairs_a_modulo_b(arr, k) == None
