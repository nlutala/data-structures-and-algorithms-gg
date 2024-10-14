"""
A file tests the sort_stack function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.stack.level2.sort_a_stack_using_a_temporary_stack import (
    sort_stack,
)


def test_sort_stack_example_1():
    """
    Example 1:
    Input : [34, 3, 31, 98, 92, 23]
    Output : [3, 23, 31, 34, 92, 98]
    """
    arr = [34, 3, 31, 98, 92, 23]
    assert sort_stack(arr) == [3, 23, 31, 34, 92, 98]


def test_sort_stack_example_2():
    """
    Example 2:
    Input : [3, 5, 1, 4, 2, 8]
    Output : [1, 2, 3, 4, 5, 8] 
    """
    arr = [3, 5, 1, 4, 2, 8]
    assert sort_stack(arr) == [1, 2, 3, 4, 5, 8]
