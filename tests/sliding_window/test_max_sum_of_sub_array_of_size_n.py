"""
A file tests the max_sum_of_subarray function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.sliding_window.max_sum_of_sub_array_of_size_n import (
    max_sum_of_subarray,
)


def test_max_sum_of_subarray() -> bool:
    """
    Input: arr = [1, 2, 6, 2, 4, 1], n = 3
    Output: 12
    """
    arr = [1, 2, 6, 2, 4, 1]
    k = 3
    assert max_sum_of_subarray(arr, k) == 12
