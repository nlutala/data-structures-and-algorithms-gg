"""
A file tests the get_missing_and_repating function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.arrays.level2.find_missing_and_repeating import (
    get_missing_and_repating,
)


def test_get_missing_and_repating_example_1():
    """
    Example 1:
    Input: arr[] = {3, 1, 3}
    Output: Missing = 2, Repeating = 3
    Explanation: In the array, 2 is missing and 3 occurs twice 
    """
    arr = [3, 1, 3]
    assert get_missing_and_repating(arr) == [2, 3]


def test_get_missing_and_repating_example_2():
    """
    Example 2:
    Input: arr[] = {4, 3, 6, 2, 1, 1}
    Output: Missing = 5, Repeating = 1
    """
    arr = [4, 3, 6, 2, 1, 1]
    assert get_missing_and_repating(arr) == [5, 1]


# Custom tests
def test_get_missing_and_repating_example_3():
    """
    Example 3:
    Input: arr[] = {4, 3, 6, 2, 1, 5, 7, 8}
    Output: Missing = None, Repeating = None
    """
    arr = [4, 3, 6, 2, 1, 5, 7, 8]
    assert get_missing_and_repating(arr) == [None, None]


def test_get_missing_and_repating_example_4():
    """
    Example 4:
    Input: arr[] = {3, 6, 2, 1, 5, 7, 8}
    Output: Missing = None, Repeating = None
    """
    arr = [3, 6, 2, 1, 5, 7, 8]
    assert get_missing_and_repating(arr) == [4, None]


def test_get_missing_and_repating_example_5():
    """
    Example 5:
    Input: arr[] = {3, 4, 6, 2, 1, 5, 7, 6, 8}
    Output: Missing = None, Repeating = None
    """
    arr = [3, 4, 6, 2, 1, 5, 7, 6, 8]
    assert get_missing_and_repating(arr) == [None, 6]
