"""
A file tests the union_and_intersection function

Author: Nathan Lutala (nlutala)
"""

from arrays.level1.union_and_intersection_of_two_soted_arrays import (
    union_and_intersection,
)


def test_union_and_intersection_1():
    """
    Example 1:
    Input: arr1[] = {1, 3, 4, 5, 7}, arr2[] = {2, 3, 5, 6}
    Output: Union : {1, 2, 3, 4, 5, 6, 7}, Intersection : {3, 5}
    """
    arr1 = [1, 3, 4, 5, 7]
    arr2 = [2, 3, 5, 6]
    u = [1, 2, 3, 4, 5, 6, 7]
    i = [3, 5]

    assert union_and_intersection(arr1, arr2) == (u, i)


def test_union_and_intersection_2():
    """
    Example 2:
    Input: arr1[] = {2, 5, 6}, arr2[] = {4, 6, 8, 10}
    Output: Union : {2, 4, 5, 6, 8, 10}, Intersection : {6}
    """
    arr1 = [1, 3, 4, 5, 7]
    arr2 = [2, 3, 5, 6]
    u = [1, 2, 3, 4, 5, 6, 7]
    i = [3, 5]

    assert union_and_intersection(arr1, arr2) == (u, i)
