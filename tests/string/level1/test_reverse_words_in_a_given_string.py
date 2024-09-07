"""
A file tests the reverse_string function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.string.level1.reverse_words_in_a_given_string import (
    reverse_string,
)


def test_reverse_string_example_1():
    """
    Example 1:
    Input: s = "i love programming very much"
    Output: s = "much very programming love i"
    """
    s = "i love programming very much"

    assert reverse_string(s) == "much very programming love i"


def test_reverse_string_example_2():
    """
    Example 2:
    Input: s = "geeks for all"
    Output: s = "all for geeks"
    """
    s = "geeks for all"

    assert reverse_string(s) == "all for geeks"
