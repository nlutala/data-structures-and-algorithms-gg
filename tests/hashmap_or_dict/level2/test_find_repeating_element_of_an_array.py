"""
A file tests the repeating_element function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.hashmap_or_dict.level2.first_repeating_element_of_an_array import (
    repeating_element,
)


def test_repeating_element_example_1():
    """
    Example 1
    Input: arr[] = {10, 5, 3, 4, 3, 5, 6}
    Output: 5
    Explanation: 5 is the first element that repeats
    """
    arr = [10, 5, 3, 4, 3, 5, 6]
    assert repeating_element(arr) == 5


def test_repeating_element_example_2():
    """
    Example 2
    Input: arr[] = {6, 10, 5, 4, 9, 120, 4, 6, 10}
    Output: 6
    Explanation: 6 is the first element that repeats
    """
    arr = [6, 10, 5, 4, 9, 120, 4, 6, 10]
    assert repeating_element(arr) == 6


# Custom tests
def test_repeating_element_example_3():
    """
    Example 3
    Input: arr[] = {1, 2, 2, 1, 3, 10}
    Output: 1
    Explanation: 1 is the first element that repeats
    """
    arr = [1, 2, 2, 1, 3, 10]
    assert repeating_element(arr) == 1


def test_repeating_element_example_4():
    """
    Example 4
    Input: arr[] = {0, 2, 3, 3, 1, 3, 2, 10}
    Output: 2
    Explanation: 2 is the first element that repeats
    """
    arr = [0, 2, 3, 3, 1, 3, 2, 10]
    assert repeating_element(arr) == 2
