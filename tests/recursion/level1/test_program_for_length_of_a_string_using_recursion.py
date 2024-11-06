"""
A file test the length function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.recursion.level1.program_for_length_of_a_string_using_recursion import (
    length,
)


def test_length_example_1():
    """
    Example 1:
    Input: str = "abcd"
    Output: 4
    """
    string = "abcd"
    assert length(string) == 4


def test_length_example_2():
    """
    Example 2:
    Input: str = "GEEKSFORGEEKS"
    Output: 13
    """
    string = "GEEKSFORGEEKS"
    assert length(string) == 13
