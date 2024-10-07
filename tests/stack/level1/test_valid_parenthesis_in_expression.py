"""
A file tests the parenthesis_checker function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.stack.level1.valid_parenthesis_in_expression import (
    parenthesis_checker,
)


def test_parenthesis_checker_example_1():
    """
    Example 1:
    Input: exp = “[()]{}{[()()]()}”
    Output: Balanced
    Explanation: all the brackets are well-formed
    """
    exp = "[()]{}{[()()]()}"
    assert parenthesis_checker(exp) == "Balanced"


def test_parenthesis_checker_example_2():
    """
    Example 2:
    Input: exp = “[(])”
    Output: Not Balanced
    Explanation: 1 and 4 brackets are not balanced because
    there is a closing ‘]’ before the closing ‘(‘
    """
    exp = "[(])"
    assert parenthesis_checker(exp) == "Not Balanced"
