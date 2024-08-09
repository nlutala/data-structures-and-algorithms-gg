"""
A file tests the find_duplicates function

Author: Nathan Lutala (nlutala)
"""

from arrays.level2.find_duplicates_in_on_time import (
    find_duplicates,
)


def test_find_duplicates_example_1():
    """
    Example 1:
    Input: array[]={1, 2, 3, 6, 3, 6, 1}
    Output: 1, 3, 6
    Explanation: The numbers 1, 3 and 6 appears more than once in the array.
    """
    arr = [1, 2, 3, 6, 3, 6, 1]

    assert find_duplicates(arr) == [1, 3, 6]


def test_find_duplicates_example_2():
    """
    Example 2:
    Input: array[] = {1, 2, 3, 4 ,3}
    Output: 3
    Explanation: The number 3 appears more than once in the array.
    """
    arr = [1, 2, 3, 4, 3]

    assert find_duplicates(arr) == [3]
