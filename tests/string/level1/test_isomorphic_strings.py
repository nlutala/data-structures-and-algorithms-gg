"""
A file tests the is_isomorphic function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.string.level1.isomorphic_strings import is_isomorphic


def test_is_isomorphic_example_1():
    """
    Example 1:
    Input:  str1 = “aab”, str2 = “xxy”
    Output: True
    Explanation: ‘a’ is mapped to ‘x’ and ‘b’ is mapped to ‘y’.
    """
    str1 = "aab"
    str2 = "xxy"
    assert is_isomorphic(str1, str2) == True


def test_is_isomorphic_example_2():
    """
    Example 2:
    Input:  str1 = “aab”, str2 = “xyz”
    Output: False
    Explanation: One occurrence of ‘a’ in str1 has ‘x’ in str2 and other occurrence of ‘a’ has ‘y’.
    """
    str1 = "aab"
    str2 = "xyz"
    assert is_isomorphic(str1, str2) == False
