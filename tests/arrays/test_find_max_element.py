"""
A file test the find_max_element function
"""
from arrays.find_the_max_or_min_element_of_an_array import (
    find_max_element, find_min_element
)


def test_find_max_element():
    """
    Example:
    Input: array[]= {1, 423, 6, 46, 34, 23, 13, 53, 4}
    Output: 423
    Explanation: The element 423 is the largest of all elements in the list.
    """
    array = [1, 423, 6, 46, 34, 23, 13, 53, 4]
    assert find_max_element(array) == max(array)


def test_find_min_element():
    """
    Example:
    Input: array[]= {1, 423, 6, 46, 34, 23, 13, 53, 4}
    Output: 1
    Explanation: The element 1 is the smallest of all elements in the list.
    """
    array = [1, 423, 6, 46, 34, 23, 13, 53, 4]
    assert find_min_element(array) == min(array)
