"""
A file tests the first_non_repeating_char function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.hashmap_or_dict.level1.non_repeating_character_of_string import (
    first_non_repeating_char,
)


def test_first_non_repeating_char_example_1():
    """
    Example 1:
    Input: S = "geeksforgeeks"
    Output: 5
    Explanation: "f" is the first character in the string which does not
    repeat.
    """
    string = "geeksforgeeks"

    return first_non_repeating_char(string) == 5


def test_first_non_repeating_char_example_2():
    """
    Example 2:
    Input: "aabbccc"
    Output: -1
    Explanation: All the characters in the given string are repeating
    """
    string = "aabbccc"

    return first_non_repeating_char(string) == -1
