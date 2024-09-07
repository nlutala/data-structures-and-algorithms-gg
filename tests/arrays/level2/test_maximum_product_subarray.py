"""
A file tests the max_product function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.arrays.level2.maximum_product_array import max_product


def test_max_product_example_1():
    """
    Example 1:
    Input: arr[] = {6, -3, -10, 0, 2}
    Output:  180
    Explanation: The subarray is {6, -3, -10}
    """
    arr = [6, -3, -10, 0, 2]

    assert max_product(arr) == 180


def test_max_product_example_2():
    """
    Example 2:
    Input: arr[] = {-1, -3, -10, 0, 60}
    Output: 60
    Explanation: The subarray is {60}
    """
    arr = [-1, -3, -10, 0, 60]

    assert max_product(arr) == 60
