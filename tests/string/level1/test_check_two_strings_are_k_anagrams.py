"""
A file tests the are_k_anagrams function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.string.level1.check_two_strings_are_k_anagrams import (
    are_k_anagrams,
)


def test_are_k_anagrams_example_1():
    """
    Example 1:
    Input:  str1 = "anagram" , str2 = "grammar" , k = 3
    Output:  Yes
    Explanation: We can update maximum 3 values and it can be done in changing
    only 'r' to 'n' and 'm' to 'a' in str2.
    """
    str1 = "anagram"
    str2 = "grammar"
    k = 3
    assert are_k_anagrams(str1, str2, k) == "Yes"


def test_are_k_anagrams_example_2():
    """
    Example 2:
    Input:  str1 = "geeks", str2 = "eggkf", k = 1
    Output:  No
    Explanation: We can update or modify only 1 value but there is a need of
    modifying 2 characters. i.e. g and f in str 2.
    """
    str1 = "geeks"
    str2 = "eggkf"
    k = 1
    assert are_k_anagrams(str1, str2, k) == "No"


def test_are_k_anagrams_example_3():
    """
    Example 2:
    Input:  str1 = "fodr", str2 = "gork", k = 2
    Output:  Yes
    Explanation: We can update or modify only 1 value but there is a need of
    modifying 2 characters. i.e. g and f in str 2.
    """
    str1 = "fodr"
    str2 = "gork"
    k = 2
    assert are_k_anagrams(str1, str2, k) == "Yes"
