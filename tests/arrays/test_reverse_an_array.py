"""
A file test the reverse_array function

Author: Nathan Lutala (nlutala)
"""
from arrays.level1.reverse_an_array import reverse_array


def test_reverse_array_example_1():
    """
    Example 1:
    Input: original_array[] = {1, 2, 3}
    Output: array_reversed[] = {3, 2, 1}
    """
    original_array = [1, 2, 3]
    assert reverse_array(original_array) == original_array[::-1]


def test_reverse_array_example_2():
    """
    Example 2:
    Input: original_array[] = {4, 5, 1, 2}
    Output: array_reversed[] = {2, 1, 5, 4}
    """
    original_array = [4, 5, 1, 2]
    assert reverse_array(original_array) == original_array[::-1]
