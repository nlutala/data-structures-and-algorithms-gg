"""
A file tests the reverse_stack function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.stack.level2.reverse_a_stack_using_recursion import (
    reverse_stack,
)


def test_reverse_stack_example_1():
    """
    Example 1:
    Input: elements present in stack from top to bottom 1 2 3 4
    Output: 4 3 2 1
    """
    arr = [1, 2, 3, 4]
    assert reverse_stack(arr) == [4, 3, 2, 1]


def test_reverse_stack_example_2():
    """
    Example 2:
    Input : [1, 2, 3]
    Output : [3, 2, 1]
    """
    arr = [1, 2, 3]
    assert reverse_stack(arr) == [3, 2, 1]
