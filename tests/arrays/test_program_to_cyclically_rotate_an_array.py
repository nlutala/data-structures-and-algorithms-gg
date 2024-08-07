"""
A file tests the cyclically_rotate_array function

Author: Nathan Lutala (nlutala)
"""

from arrays.level2.program_to_cyclically_rotate_an_array import (
    cyclically_rotate_array,
)


def test_cyclically_rotate_array_example_1():
    """
    Example 1:
    Input: arr[] = {1, 2, 3, 4, 5}
    Output: arr[] = {5, 1, 2, 3, 4}
    """
    arr = [1, 2, 3, 4, 5]

    assert cyclically_rotate_array(arr) == [5, 1, 2, 3, 4]


def test_cyclically_rotate_array_example_2():
    """
    Example 2:
    Input: arr[] = {2, 3, 4, 5, 1}
    Output: {1, 2, 3, 4, 5}
    """
    arr = [2, 3, 4, 5, 1]

    assert cyclically_rotate_array(arr) == [1, 2, 3, 4, 5]
