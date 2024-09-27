"""
A file test the factorial function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.recursion.level1.factorial_of_a_number import factorial


def test_factorial_example_1():
    """
    Example 1:
    Input: n = 5
    Output: 120
    Explanation: 5! = 5 * 4 * 3 * 2 * 1 = 120
    """
    n = 5
    assert factorial(n) == 120


def test_factorial_example_2():
    """
    Example 2:
    Input: n = 4
    Output: 24
    Explanation: 4! = 4 * 3 * 2 * 1 = 24
    """
    n = 4
    assert factorial(n) == 24


def test_factorial_example_3():
    """
    Example 3:
    Input: n = 0
    Output: 1
    """
    n = 0
    assert factorial(n) == 1


def test_factorial_example_4():
    """
    Example 4:
    Input: n = 1
    Output: 1
    """
    n = 1
    assert factorial(n) == 1
