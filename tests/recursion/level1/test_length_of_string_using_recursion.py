"""
A file test the string_length function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.recursion.level1.length_of_string_using_recursion import (
    string_length,
)


def test_string_length_example_1():
    """
    Example 1:
    Input: string = "abcd"
    Output: 4
    """
    string = "abcd"
    assert string_length(string) == 4


def test_string_length_example_2():
    """
    Example 2:
    Input: string = "GEEKSFORGEEKS"
    Output: 13
    """
    string = "GEEKSFORGEEKS"
    assert string_length(string) == 13
