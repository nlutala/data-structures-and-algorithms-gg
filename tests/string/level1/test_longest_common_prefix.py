"""
A file tests the longest_prefix function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.string.level1.longest_common_prefix import (
    longest_prefix,
)


def test_longest_prefix_example_1():
    """
    Example 1:
    Input: strs[] = [“geeksforgeeks”, “geeks”, “geek”, “geezer”]
    Output: gee
    Explanation: “gee” is the longest common prefix in all the given strings.
    """
    strs = ["geeksforgeeks", "geeks", "geek", "geezer"]

    return longest_prefix(strs) == "gee"


def test_longest_prefix_example_2():
    """
    Example 2:
    Input: strs[] = ["hello", "world"]
    Output: -1
    Explanation: There's no common prefix in the given strings.
    """
    strs = ["hello", "world"]

    return longest_prefix(strs) == -1
