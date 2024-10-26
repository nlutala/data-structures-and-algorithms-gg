"""
A file tests the atoi function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.string.level2.implement_atoi import atoi


def test_atoi_example_1():
    """
    Example 1:
    Input: s = “-123”
    Output: –123
    """
    s = "-123"
    assert atoi(s) == -123


def test_atoi_example_2():
    """
    Example 2:
    Input: s = ”   -“
    Output: 0
    Explanation: No digits are present, therefore 0.
    """
    s = "   -"
    assert atoi(s) == 0


def test_atoi_example_3():
    """
    Example 3:
    Input: s = ”  1231231231311133″
    Output: 2147483647
    Explanation: The converted number is greater than 231 – 1, therefore print
    2^31 – 1 = 2147483647.
    """
    s = "  1231231231311133"
    assert atoi(s) == (2**31) - 1


def test_atoi_example_4():
    """
    Example 4:
    Input: s = “-999999999999”
    Output: -2147483648
    Explanation: The converted number is smaller than -231, therefore print
    -231 = -2147483648.
    """
    s = "-999999999999"
    assert atoi(s) == (2**31) * -1


def test_atoi_example_5():
    """
    Example 5:
    Input: s = ”  -0012gfg4″
    Output: -12
    Explanation: Nothing is read after -12 as a non-digit character ‘g’ was
    encountered.
    """
    s = "  -0012gfg4"
    assert atoi(s) == -12
