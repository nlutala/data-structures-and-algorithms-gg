"""
A file tests the longest_subarray function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.sliding_window.longest_subarray_with_sum_k import longest_subarray


def test_longest_subarray_example_1() -> None:
    """
    Example 1
    Input: arr[] = { 10, 5, 2, 7, 1, 9 }, k = 15
    Output: 4
    Explanation: The sub-array is {5, 2, 7, 1}.
    """
    arr = [10, 5, 2, 7, 1, 9]
    k = 15
    assert longest_subarray(arr, k) == 4


def test_longest_subarray_example_2() -> None:
    """
    Example 2
    Input: arr[] = {-5, 8, -14, 2, 4, 12}, k = -5
    Output: 5
    """
    arr = [-5, 8, -14, 2, 4, 12]
    k = -5
    assert longest_subarray(arr, k) == 5
