"""
A file test the mean function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.recursion.mean_of_array_using_recursion import mean


def test_mean_example_1():
    """
    Example 1:
    Input : [1, 2, 3, 4, 5]
    Output : 3
    """
    arr = [1, 2, 3, 4, 5]
    assert mean(arr) == 3


def test_mean_example_2():
    """
    Example 1:
    Input : [1, 2, 3]
    Output : 2
    """
    arr = [1, 2, 3]
    assert mean(arr) == 2
