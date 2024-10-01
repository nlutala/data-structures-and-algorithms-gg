"""
A file test the remove_duplicates function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.recursion.level2.remove_all_adjacent_duplicates import (
    remove_duplicates,
)


def test_remove_duplicates_example_1():
    """
    Example 1:
    Input: S = "geeksforgeek"
    Output: "gksforgk"
    Explanation: g(ee)ksforg(ee)k -> gksforgk
    """
    assert remove_duplicates("geeksforgeek") == "gksforgk"


def test_remove_duplicates_example_2():
    """
    Example 2:
    Input: S = "abccbccba"
    Output: ""
    Explanation: ab(cc)b(cc)ba->abbba->a(bbb)a->aa->(aa)->"" (empty string)
    """
    assert remove_duplicates("abccbccba") == ""
