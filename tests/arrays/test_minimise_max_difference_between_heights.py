"""
A file tests the min_max_difference function

Author: Nathan Lutala (nlutala)
"""

from arrays.level2.minimise_max_difference_between_heights import (
    min_max_difference,
)


def test_min_max_difference_example_1():
    """
    Example 1:
    Input: arr[] = {1, 15, 10}, k = 6
    Output:  Maximum difference is 5.
    Explanation: Change 1 to 7, 15 to 9 and 10 to 4. Maximum difference is 5
    (between 4 and 9). We can’t get a lower difference.
    """
    arr = [1, 15, 10]
    k = 6

    assert min_max_difference(arr, k)


def test_min_max_difference_example_2():
    """
    Example 2:
    Input: arr[] = {1, 5, 15, 10}, k = 3   
    Output: Maximum difference is 8, arr[] = {4, 8, 12, 7}
    """
    arr = [1, 5, 15, 10]
    k = 3

    assert min_max_difference(arr, k)
