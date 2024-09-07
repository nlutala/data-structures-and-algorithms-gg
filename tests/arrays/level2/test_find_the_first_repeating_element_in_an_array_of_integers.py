"""
A file tests the find_first_repeating_integer function

Author: Nathan Lutala (nlutala)
"""

from arrays.level2.find_the_first_repeating_element_in_an_array_of_integers import (
    find_first_repeating_integer,
)


def test_find_first_repeating_integer_example_1():
    """
    Example 1:
    Input: arr[] = {10, 5, 3, 4, 3, 5, 6}
    Output: 5
    Explanation: 5 is the first element that repeats
    """
    arr = [10, 5, 3, 4, 3, 5, 6]

    assert find_first_repeating_integer(arr) == 5


def test_find_first_repeating_integer_example_2():
    """
    Example 2:
    Input: arr[] = {6, 10, 5, 4, 9, 120, 4, 6, 10}
    Output: 6 
    Explanation: 6 is the first element that repeats
    """
    arr = [6, 10, 5, 4, 9, 120, 4, 6, 10]

    assert find_first_repeating_integer(arr) == 6
