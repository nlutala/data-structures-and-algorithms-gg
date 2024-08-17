"""
A file tests the rearrange_array_in_positive_and_negative function

Author: Nathan Lutala (nlutala)
"""

from arrays.level2.rearrange_array_in_alternating_positive_and_negative_items import (
    rearrange_array_in_positive_and_negative,
)


def test_rearrange_array_in_positive_and_negative_example_1():
    """
    Example 1:
    Input:  arr[] = {1, 2, 3, -4, -1, 4}
    Output: arr[] = {-4, 1, -1, 2, 3, 4}
    """
    arr = [1, 2, 3, -4, -1, 4]
    output = [-4, 1, -1, 2, 3, 4]

    assert rearrange_array_in_positive_and_negative(arr) == output


def test_rearrange_array_in_positive_and_negative_example_2():
    """
    Example 2:
    Input:  arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
    Output: arr[] = {-5, 5, -2, 2, -8, 4, 7, 1, 8, 0}
    """
    arr = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]

    assert rearrange_array_in_positive_and_negative(arr) == [
        -5,
        5,
        -2,
        2,
        -8,
        4,
        7,
        1,
        8,
        0,
    ]
