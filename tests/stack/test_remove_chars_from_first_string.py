"""
A file tests the remove_chars function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.stack.remove_chars_from_first_string import (
    remove_chars,
)


def test_remove_chars_example_1():
    """
    Example 1:
    Input:
    string1 = “computer”
    string2 = “cat”
    Output: “ompuer”
    Explanation: After removing characters(c, a, t)
    from string1 we get “ompuer”.
    """
    return remove_chars("computer", "cat") == "ompuer"


def test_remove_chars_example_2():
    """
    Example 2:
    Input:
    string1 = “occurrence”
    string2 = “car”
    Output: “ouene”
    Explanation: After removing characters
    (c, a, r) from string1 we get “ouene”.
    """
    return remove_chars("occurrence", "car") == "ouene"
