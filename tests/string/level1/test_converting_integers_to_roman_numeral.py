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
    Input: 1904
    Output: MCMIV
    Explanation: MCMIV is a Roman symbol which represents 1094
    """
    s = 1904
    assert int_to_roman_numeral(s) == "MCMIV"


def test_int_to_roman_numeral_example_4():
    """
    Example 4:
    Input: 3549
    Output: MMMDXLIX
    """
    s = 3549
    assert int_to_roman_numeral(s) == "MMMDXLIX"


# Some more custom tests of my own
def test_int_to_roman_numeral_example_5():
    """
    Example 5:
    Input: 2024
    Output: MMXXIV
    """
    s = 2024
    assert int_to_roman_numeral(s) == "MMXXIV"


def test_int_to_roman_numeral_example_6():
    """
    Example 6:
    Input: 1990
    Output: MCMXC
    """
    s = 1990
    assert int_to_roman_numeral(s) == "MCMXC"


def test_int_to_roman_numeral_example_7():
    """
    Example 7:
    Input: 2000
    Output: MM
    """
    s = 2000
    assert int_to_roman_numeral(s) == "MM"
