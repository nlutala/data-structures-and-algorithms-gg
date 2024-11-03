"""
A file tests the delete_chars function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.stack.level1.delete_chars_from_the_beginning import (
    delete_chars,
)


def test_delete_chars_example_1():
    """
    Example 1:
    Input: string1 = “computer”, string2 = “cat”
    Output: “ompuer”
    Explanation: After removing characters(c, a, t) from string1 we get
    “ompuer”.
    """
    string1, string2 = "computer", "cat"
    assert delete_chars(string1, string2) == "ompuer"


def test_delete_chars_example_2():
    """
    Example 2:
    Input: string1 = “occurrence”, string2 = “car”
    Output: “ouene”
    Explanation: After removing characters (c, a, r) from string1 we get
    “ouene”.
    """
    string1, string2 = "occurrence", "car"
    assert delete_chars(string1, string2) == "ouene"
