"""
A file tests the remove_duplicates function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.hashmap_or_dict.level1.remove_duplicates_from_sorted_array import (
    remove_duplicates,
)


def test_remove_duplicates_example_1():
    """
    Example 1
    Input: arr[] = {2, 2, 2, 2, 2}
    Output: arr[] = {2}
    Explanation: All the elements are 2, So only keep one instance of 2.
    """
    arr = [2, 2, 2, 2, 2]
    assert remove_duplicates(arr) == [2]


def test_remove_duplicates_example_2():
    """
    Example 2
    Input: arr[] = {1, 2, 2, 3, 4, 4, 4, 5, 5}
    Output: arr[] = {1, 2, 3, 4, 5}
    """
    arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
    assert remove_duplicates(arr) == [1, 2, 3, 4, 5]


def test_remove_duplicates_example_3():
    """
    Example 3
    Input: arr[] = {1, 2, 3}
    Output : arr[] = {1, 2, 3}
    Explanation : No change as all elements are distinct
    """
    arr = [1, 2, 3]
    assert remove_duplicates(arr) == [1, 2, 3]
