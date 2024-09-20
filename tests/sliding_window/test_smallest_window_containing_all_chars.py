"""
A file tests the window_with_all_chars function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.sliding_window.smallest_window_containing_all_chars import (
    window_with_all_chars,
)


def test_window_with_all_chars_example_1() -> None:
    """
    Example 1
    Input: aabcbcdbca
    Output: dbca
    Explanation:
    Possible substrings= {aabcbcd, abcbcd,
    bcdbca, dbca....}
    Of the set of possible substrings 'dbca'
    is the shortest substring having all the
    distinct characters of given string.
    """
    string = "aabcbcdbca"
    assert window_with_all_chars(string) == "dbca"


def test_window_with_all_chars_example_2() -> None:
    """
    Example 2
    Input: aaab
    Output: ab
    Explanation:
    Possible substrings={aaab, aab, ab}
    Of the set of possible substrings 'ab'
    is the shortest substring having all
    the distinct characters of given string.
    """
    string = "aaab"
    assert window_with_all_chars(string) == "ab"
