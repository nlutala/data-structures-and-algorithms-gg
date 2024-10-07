"""
A file tests the min_product and min_product_no_heap functions

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.heaps.level1.min_product_of_k_int import (
    min_product,
    min_product_no_heap,
)


def test_min_product_no_heap_example_1():
    """
    Example 1:
    Input: arr[] = {198, 76, 544, 123, 154, 675}, K = 2
    Output: 9348
    Explanation: We get minimum product after multiplying 76 and 123.
    """
    arr = [198, 76, 544, 123, 154, 675]
    k = 2
    assert min_product_no_heap(arr, k) == 9348


def test_find_kth_smallest_no_heap_example_2():
    """
    Example 2:
    Input: arr[] = {11, 8, 5, 7, 5, 100}, K = 4
    Output: 1400
    """
    arr = [11, 8, 5, 7, 5, 100]
    k = 4
    assert min_product_no_heap(arr, k) == 1400


def test_min_product_example_1():
    """
    Example 1:
    Input: arr[] = {198, 76, 544, 123, 154, 675}, K = 2
    Output: 9348
    Explanation: We get minimum product after multiplying 76 and 123.
    """
    arr = [198, 76, 544, 123, 154, 675]
    k = 2
    assert min_product(arr, k) == 9348


def test_min_product_example_2():
    """
    Example 2:
    Input: arr[] = {11, 8, 5, 7, 5, 100}, K = 4
    Output: 1400
    """
    arr = [11, 8, 5, 7, 5, 100]
    k = 4
    assert min_product(arr, k) == 1400
