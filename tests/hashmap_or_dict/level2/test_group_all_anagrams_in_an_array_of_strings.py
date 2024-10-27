"""
A file tests the group_anagrams function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.hashmap_or_dict.level2.group_all_anagrams_in_an_array_of_strings import (
    group_anagrams,
)


def test_group_anagrams_example_1():
    """
    Example 1
    Input :   {"cat", "dog", "tac", "god", "act"}
    Output :  {"cat",  "tac",  "act",  "dog",  "god"}
    """
    arr = ["cat", "dog", "tac", "god", "act"]
    assert group_anagrams(arr) == ["cat", "tac", "act", "dog", "god"]
