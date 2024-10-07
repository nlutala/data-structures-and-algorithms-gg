"""
A file tests the reverse_stack function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.stack.level1.reverse_a_stack_using_queue import reverse_stack


def test_reverse_stack_example_1():
    """
    Example 1:
    Input: Stack: (Top to Bottom) [10 -> 20 -> 30 -> 40]
    Output: Stack: (Top to Bottom) [40 -> 30 -> 20 -> 10]
    """
    stack = [10, 20, 30, 40]
    return reverse_stack(stack) == [40, 30, 20, 10]


def test_reverse_stack_example_2():
    """
    Example 2:
    Input:  Stack: [6 -> 5 -> 4]
    Output: Stack: [4 -> 5 -> 6]
    """
    stack = [6, 5, 4]
    return reverse_stack(stack) == [4, 5, 6]
