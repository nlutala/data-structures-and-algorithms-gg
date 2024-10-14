"""
A file tests the subarrays_with_zero_sum function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.hashmap_or_dict.level2.print_all_subarrays_with_zero_sum import (
    subarrays_with_zero_sum,
)


def test_subarrays_with_zero_sum_example_1():
    """
    Example 1
    Input: arr = [6, 3, -1, -3, 4, -2, 2, 4, 6, -12, -7]
    Output:
    Subarray found from Index 2 to 4
    Subarray found from Index 2 to 6
    Subarray found from Index 5 to 6
    Subarray found from Index 6 to 9
    Subarray found from Index 0 to 10
    """
    arr = [6, 3, -1, -3, 4, -2, 2, 4, 6, -12, -7]
    assert subarrays_with_zero_sum(arr) == [[5, 6], [2, 4], [6, 9], [2, 6], [0, 10]]


def test_subarrays_with_zero_sum_example_2():
    """
    Example 2
    Input: arr = [1, 2, -3, 3, -1, -1]
    Output:
    Subarray found from Index 0 to 2
    Subarray found from Index 2 to 3
    Subarray found from Index 1 to 5
    """
    arr = [1, 2, -3, 3, -1, -1]
    assert subarrays_with_zero_sum(arr) == [[2, 3], [0, 2], [1, 5]]


# Custom tests
def test_subarrays_with_zero_sum_example_3():
    """
    Example 3
    Input: arr = [1, 1, 1, 1, 0, -1]
    Output:
    Subarray found from Index 3 to 5
    """
    arr = [1, 1, 1, 1, 0, -1]
    assert subarrays_with_zero_sum(arr) == [[3, 5]]


def test_subarrays_with_zero_sum_example_4():
    """
    Example 3
    Input: arr = [1, 1, 0, -1, -2, 1]
    Output:
    Subarray found from Index 1 to 3
    Subarray found from Index 0 to 5
    """
    arr = [1, 1, 0, -1, -2, 1]
    assert subarrays_with_zero_sum(arr) == [[1, 3], [0, 5]]


def test_subarrays_with_zero_sum_example_5():
    """
    Example 3
    Input: arr = [1, 5, 2, 0, -1, -7, 1, -1]
    Output:
    Subarray found from Index 6 to 7
    Subarray found from Index 0 to 5
    Subarray found from Index 1 to 6
    Subarray found from Index 0 to 7
    """
    arr = [1, 5, 2, 0, -1, -7, 1, -1]
    assert subarrays_with_zero_sum(arr) == [[6, 7], [0, 5], [1, 6], [0, 7]]
