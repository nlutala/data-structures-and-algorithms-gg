"""
A file tests the sort_array012 function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.arrays.level1.sort_an_array_of_zeros import sort_array_012


def test_count_occurences_example_1():
    """
    Example 1:
    Input: {0, 1, 2, 0, 1, 2}
    Output: {0, 0, 1, 1, 2, 2}
    Explanation: {0, 0, 1, 1, 2, 2} has all 0s first, then all 1s and all 2s
    in last.
    """
    arr = [0, 1, 2, 0, 1, 2]

    assert sort_array_012(arr) == [0, 0, 1, 1, 2, 2]


def test_count_occurences_example_2():
    """
    Input: {0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1}
    Output: {0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2}
    Explanation: {0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2} has all 0s first, then
    all 1s and all 2s in last.
    """
    arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]

    assert sort_array_012(arr) == [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]
