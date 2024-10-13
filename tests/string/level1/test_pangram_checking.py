"""
A file tests the is_pangram function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.string.level1.pangram_checking import is_pangram


def test_is_pangram_example_1():
    """
    Example 1:
    Input: “The quick brown fox jumps over the lazy dog” 
    Output: is a Pangram 
    Explanation: Contains all the characters from ‘a’ to ‘z’] 
    """
    s = "The quick brown fox jumps over the lazy dog"
    assert is_pangram(s) == "is a Pangram"


def test_is_pangram_example_2():
    """
    Example 2:
    Input: “The quick brown fox jumps over the dog”
    Output: is not a Pangram 
    Explanation: Doesn’t contain all the characters from ‘a’ to ‘z’, as ‘l’, 
    ‘z’, ‘y’ are missing
    """
    s = "The quick brown fox jumps over the dog"
    assert is_pangram(s) == "is not a Pangram"
