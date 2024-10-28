"""
A file test the decimal_to_binary function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.recursion.level1.decimal_to_binary_using_recursion import (
    decimal_to_binary,
)


def test_decimal_to_binary_example_1():
    """
    Example 1:
    Input: 7
    Output: 111
    """
    decimal = 7
    assert decimal_to_binary(decimal) == "111"


def test_decimal_to_binary_example_2():
    """
    Example 2:
    Input: 10
    Output: 1010
    """
    decimal = 10
    assert decimal_to_binary(decimal) == "1010"


# Custom tests
def test_decimal_to_binary_example_3():
    """
    Example 3:
    Input: 1048576
    Output: 100000000000000000000
    """
    decimal = 1048576
    assert decimal_to_binary(decimal) == "100000000000000000000"


def test_decimal_to_binary_example_4():
    """
    Example 4:
    Input: 17
    Output: 10001
    """
    decimal = 17
    assert decimal_to_binary(decimal) == "10001"
