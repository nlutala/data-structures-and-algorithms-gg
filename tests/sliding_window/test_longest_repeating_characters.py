"""
A file tests the longest_repeat function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.sliding_window.longest_repeating_characters import longest_repeat


def test_longest_repeat_example_1() -> None:
    """
    Example 1
    Input: “ABCBC”
    Output: 3
    Explanation: The longest substring without repeating characters is “ABC”
    """
    s = "ABCBC"
    assert longest_repeat(s) == "ABC"


def test_longest_repeat_example_2() -> None:
    """
    Example 2
    Input: “AAA”
    Output: 1
    Explanation: The longest substring without repeating characters is “A”
    """
    s = "AAA"
    assert longest_repeat(s) == "A"


def test_longest_repeat_example_3() -> None:
    """
    Example 3
    Input: “GEEKSFORGEEKS”
    Output: 7
    Explanation: The longest substrings without repeating characters are “EKSFORG” and
    “KSFORGE”, with lengths of 7.
    """
    s = "GEEKSFORGEEKS"
    assert longest_repeat(s) == "EKSFORG" or longest_repeat(s) == "KSFORGE"
