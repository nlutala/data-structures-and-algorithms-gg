"""
A file test the is_palindrome function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.recursion.level1.string_is_palindrome import is_palindrome


def test_is_palindrome_example_1():
    """
    Example 1:
    Input: malayalam
    Output: Yes
    Explanation: Reverse of malayalam is also malayalam.
    """
    string = "malayalam"
    assert is_palindrome(string) is True


def test_is_palindrome_example_2():
    """
    Example 2:
    Input : max
    Output : No
    Explanation: Reverse of max is not max.
    """
    string = "max"
    assert is_palindrome(string) is False
