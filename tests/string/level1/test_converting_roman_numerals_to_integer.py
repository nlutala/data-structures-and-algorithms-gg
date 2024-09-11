"""
A file tests the roman_number_to_int function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.string.level1.converting_roman_numerals_to_integer import (
    roman_number_to_int,
)


def test_roman_number_to_int_example_1():
    """
    Example 1:
    Input: IX
    Output: 9
    Explanation: IX is a Roman symbol which represents 9
    """
    s = "IX"
    assert roman_number_to_int(s) == 9


def test_roman_number_to_int_example_2():
    """
    Example 2:
    Input: XL
    Output: 40
    Explanation: XL is a Roman symbol which represents 40
    """
    s = "XL"
    assert roman_number_to_int(s) == 40


def test_roman_number_to_int_example_3():
    """
    Example 3:
    Input: MCMIV
    Output: 1904
    Explanation: MCMIV is a Roman symbol which represents 1094
    """
    s = "MCMIV"
    assert roman_number_to_int(s) == 1904
