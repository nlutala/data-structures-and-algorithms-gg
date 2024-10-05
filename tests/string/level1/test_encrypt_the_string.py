"""
A file tests the encrypt_string function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.string.level1.encrypt_the_string import encrypt_string


def test_encrypt_string_example_1():
    """
    Example 1:
    Input: S = “aaaaaaaaaaa”
    Output: ba
    Explanation:
    1. First convert the given string to “a11” i.e. write, character along
       with its frequency.
    2. Then, change “a11” to “ab” because 11 is b in hexadecimal.
    3. Then, finally reverse the string i.e “ba”.
    """
    s = "aaaaaaaaaaa"
    assert encrypt_string(s) == "ba"


def test_encrypt_string_example_2():
    """
    Example 2:
    Input: S = “abc”
    Output: 1c1b1a
    """
    s = "abc"
    assert encrypt_string(s) == "1c1b1a"
