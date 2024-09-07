"""
A file tests the find_subarray_with_sum function

Author: Nathan Lutala (nlutala)
"""

from arrays.level1.move_all_negative_numbers_to_beginning_and_positive_to_end import (
    move_negative_and_positive,
)


def test_move_negative_and_positive():
    """
    Input: [-12, 11, -13, -5, 6, -7, 5, -3, -6]
    Output: [-12, -13, -5, -7, -3, -6, 11, 6, 5]
    zero_index += 1
    """
    arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]

    assert sum(move_negative_and_positive(arr)[0:7]) < 0
