"""
A file tests the evaluate_postfix function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.stack.level2.evaluate_postfix_expression import evaluate_postfix


def test_evaluate_postfix_example_1():
    """
    Example 1:
    Input: str = “2 3 1 * + 9 -“
    Output: -4
    Explanation: If the expression is converted into an infix expression, it will be
    2 + (3 * 1) – 9 = 5 – 9 = -4.
    """
    expression = "2 3 1 * + 9 -"
    assert evaluate_postfix(expression) == -4


def test_evaluate_postfix_example_2():
    """
    Example 2:
    Input: str = “100 200 + 2 / 5 * 7 +”
    Output: 757
    """
    expression = "100 200 + 2 / 5 * 7 +"
    assert evaluate_postfix(expression) == 757
