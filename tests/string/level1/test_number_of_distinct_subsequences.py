"""
A file tests the count_subsequences function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.string.level1.number_of_distinct_subsequences import (
    count_subsequences,
)


def test_count_subsequences_example_1():
    """
    Example 1:
    Input: str = “gfg”
    Output: 7
    Explanation: The seven distinct subsequences are “”, “g”, “f”, “gf”, “fg”,
    “gg” and “gfg”
    """
    string = "gfg"
    assert count_subsequences(string) == 7


def test_count_subsequences_example_2():
    """
    Example 2:
    Input: str = “ggg”
    Output: 4
    Explanation: The four distinct subsequences are “”, “g”, “gg” and “ggg”
    """
    string = "ggg"
    assert count_subsequences(string) == 4


# Custom test
def test_count_subsequences_example_3():
    """
    Example 3:
    Input: str = “abab”
    Output: 12
    """
    string = "abab"
    assert count_subsequences(string) == 12
