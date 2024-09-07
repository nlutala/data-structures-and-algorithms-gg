"""
A file tests the min_elem function

Author: Nathan Lutala (nlutala)
"""

from arrays.level2.minimum_element_in_a_sorted_and_rotated_array import min_elem


def test_min_elem_example_1():
    """
    Example 1:
    Input: arr[] = {5, 6, 1, 2, 3, 4}
    Output: 1
    Explanation: 1 is the minimum element present in the array.
    """
    arr = [5, 6, 1, 2, 3, 4]

    assert min_elem(arr) == 1


def test_min_elem_example_2():
    """
    Example 2:
    Input: arr[] = {1, 2, 3, 4}
    Output: 1
    """
    arr = [1, 2, 3, 4]

    assert min_elem(arr) == 1


def test_min_elem_example_3():
    """
    Example 3:
    Input: arr[] = {2, 1}
    Output: 1
    """
    arr = [2, 1]

    assert min_elem(arr) == 1
