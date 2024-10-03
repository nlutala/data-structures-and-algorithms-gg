"""
A file tests the is_divisble_by_7 function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.string.level1.divisible_by_seven import is_divisble_by_7


def test_is_divisble_by_7_example_1():
    """
    Example 1:
    Input: 371
    Output: True
    """
    assert is_divisble_by_7(371) == True


# Custom tests I added
def test_is_divisble_by_7_example_2():
    """
    Example 2:
    Input: -17
    Output: False
    """
    assert is_divisble_by_7(-17) == False


def test_is_divisible_by_7_example_3():
    """
    Example 2:
    Input: 0
    Output: True
    """
    assert is_divisble_by_7(0) == True
