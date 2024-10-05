"""
A file tests the remove_middle_elem function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.stack.delete_middle_element_of_a_stack import (
    remove_middle_elem,
)


def test_remove_middle_elem_example_1():
    """
    Example 1:
    Input  : Stack[] = [1, 2, 3, 4, 5]
    Output : Stack[] = [1, 2, 4, 5]
    """
    stack = [1, 2, 3, 4, 5]
    assert remove_middle_elem(stack) == [1, 2, 4, 5]


def test_remove_middle_elem_example_2():
    """
    Example 2:
    Input  : Stack[] = [1, 2, 3, 4, 5, 6]
    Output : Stack[] = [1, 2, 4, 5, 6]
    """
    stack = [1, 2, 3, 4, 5, 6]
    assert remove_middle_elem(stack) == [1, 2, 4, 5, 6]
