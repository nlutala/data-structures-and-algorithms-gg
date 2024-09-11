"""
A file tests the int_to_roman_numeral function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.string.level1.converting_integers_to_roman_numeral import (
    int_to_roman_numeral,
)


def test_int_to_roman_numeral_example_1():
    """
    Example 1:
    Input: 9
    Output: IX
    Explanation: IX is a Roman symbol which represents 9
    """
    s = 9
    assert int_to_roman_numeral(s) == "IX"


def test_int_to_roman_numeral_example_2():
    """
    Example 2:
    Input: 40
    Output: XL
    Explanation: XL is a Roman symbol which represents 40
    """
    s = 40
    assert int_to_roman_numeral(s) == "XL"


def test_int_to_roman_numeral_example_3():
    """
    Example 3:
    Input: MCMIV
    Output: 1904
    Explanation: MCMIV is a Roman symbol which represents 1094
    """
    s = 1904
    assert int_to_roman_numeral(s) == "MCMIV"
