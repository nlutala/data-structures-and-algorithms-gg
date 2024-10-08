"""
A file tests the find_max_of_subarray function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.sliding_window.find_max_sum_of_a_subarray import find_max_of_subarray


def test_find_max_of_subarray_example_1() -> None:
    """
    Example 1
    Input  : arr[] = {100, 200, 300, 400},  k = 2
    Output : 700
    """
    arr = [100, 200, 300, 400]
    k = 2
    assert find_max_of_subarray(arr, k) == 700


def test_find_max_of_subarray_example_2() -> None:
    """
    Example 2
    Input  : arr[] = {1, 4, 2, 10, 23, 3, 1, 0, 20}, k = 4
    Output : 39
    Explanation: We get maximum sum by adding subarray {4, 2, 10, 23} of size 4.
    """
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 4
    assert find_max_of_subarray(arr, k) == 39


def test_find_max_of_subarray_example_3() -> None:
    """
    Example 3
    Input  : arr[] = {2, 3}, k = 3
    Output : Invalid
    Explanation: There is no subarray of size 3 as size of whole array is 2.
    """
    arr = [2, 3]
    k = 3
    assert find_max_of_subarray(arr, k) == "Invalid"


# More test cases were found here: https://www.geeksforgeeks.org/largest-sum-subarray-least-k-numbers/
def test_find_max_of_subarray_example_4() -> None:
    """
    Example 4
    Input  : arr[] = {-4, -2, 1, -3}, k = 2
    Output : -1
    Explanation: The sub array is [-2, -1].
    """
    arr = [-4, -2, 1, -3]
    k = 2
    assert find_max_of_subarray(arr, k) == -1


def test_find_max_of_subarray_example_5() -> None:
    """
    Example 5
    Input  : Input : arr[] = {1, 1, 1, 1, 1, 1}, k = 2
    Output : 2
    Explanation: The sub array is [1, 1].
    """
    arr = [1, 1, 1, 1, 1, 1]
    k = 2
    assert find_max_of_subarray(arr, k) == 2


def test_find_max_of_subarray_example_6() -> None:
    """
    Example 6
    Input  : Input : arr[] = {1, 2, 3, -10, -3}, k = 4
    Output : -4
    """
    arr = [1, 2, 3, -10, -3]
    k = 4
    assert find_max_of_subarray(arr, k) == -4
