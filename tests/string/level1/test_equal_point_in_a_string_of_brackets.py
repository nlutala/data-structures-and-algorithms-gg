"""
A file tests the equal_point function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.string.level1.equal_point_in_a_string_of_brackets import (
    equal_point,
)


def test_equal_point_example_1():
    """
    Example 1:
    Input: str = “(())))(“
    Output: 4
    Explanation: After index 4, string splits into (()) and ))(. The number of
    opening brackets in the first part is equal to the number of closing
    brackets in the second part.
    """
    string = "(())))("
    assert equal_point(string) == 4


def test_equal_point_example_2():
    """
    Example 2:
    Input: str = “))”
    Output: 2
    Explanation: As after 2nd position i.e. )) and “empty” string will be
    split into these two parts. So, in this number of opening brackets i.e. 0
    in the first part is equal to the number of closing brackets in the second
    part i.e. also 0.
    """
    string = "(())))("
    assert equal_point(string) == 4


def test_equal_point_example_3():
    """
    Example 3:
    Input: str = "(()))(()()())))"
    Output: 9
    """
    string = "(()))(()()())))"
    assert equal_point(string) == 9
