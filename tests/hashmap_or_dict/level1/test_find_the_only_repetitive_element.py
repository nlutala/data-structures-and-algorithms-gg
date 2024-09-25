"""
A file tests the find_repeated_element function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.hashmap_or_dict.level1.find_the_only_repetitive_element import (
    find_repeated_element,
)


def test_find_repeated_element_example_1():
    """
    Example 1
    Input: arr[] = {1, 3, 2, 3, 4}
    Output: 3
    Explanation: The number 3 is the only repeating element.
    """
    arr = [1, 3, 2, 3, 4]
    assert find_repeated_element(arr) == 3


def test_find_repeated_element_example_2():
    """
    Example 2
    Input: arr[] = {1, 5, 1, 2, 3, 4}
    Output: 1
    """
    arr = [1, 5, 1, 2, 3, 4]
    assert find_repeated_element(arr) == 1
