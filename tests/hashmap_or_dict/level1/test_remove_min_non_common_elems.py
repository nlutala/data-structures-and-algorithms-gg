"""
A file tests the no_common_elems function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.hashmap_or_dict.level1.remove_min_non_common_elems import (
    no_common_elems,
)


def test_no_common_elems_example_1():
    """
    Example 1
    Input: arr1[] = {1, 2, 3, 4}, arr2[] = {2, 3, 4, 5, 8}
    Output: 3
    Explanation: We need to remove 2, 3 and 4 from any array.
    """
    arr1 = [1, 2, 3, 4]
    arr2 = [2, 3, 4, 5, 8]

    assert no_common_elems(arr1, arr2) == 3


def test_no_common_elems_example_2():
    """
    Example 2
    Input: arr[] = { 4, 2, 4, 4}, arr2[] = { 4, 3 }
    Output: 1
    Explanation: We need to remove 4 from arr2[]
    """
    arr1 = [4, 2, 4, 4]
    arr2 = [4, 3]

    assert no_common_elems(arr1, arr2) == 1


def test_no_common_elems_example_3():
    """
    Example 3
    Input : arr[] = { 1, 2, 3, 4 }, arr2[] = { 5, 6, 7 }
    Output : 0
    Explanation: There is no common element in both.
    """
    arr1 = [1, 2, 3, 4]
    arr2 = [5, 6, 7]

    assert no_common_elems(arr1, arr2) == 0
