"""
A file tests the k_closest_elements function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.heaps.level2.find_k_closest_numbers import (
    k_closest_elements,
)


def test_find_kth_largest_elements_example_1():
    """
    Example 1:
    Input: K = 4, X = 35
       arr[] = {12, 16, 22, 30, 35, 39, 42,
               45, 48, 50, 53, 55, 56}
    Output: 30 39 42 45
    """
    k, x, arr = 4, 35, [12, 16, 22, 30, 35, 39, 42, 45, 48, 50, 53, 55, 56]
    assert k_closest_elements(k, x, arr) == [30, 39, 42, 45]


# Custom tests
def test_find_kth_largest_elements_example_2():
    """
    Example 2:
    Input: K = 3, X = 20
       arr[] = {12, 16, 22, 30, 35, 39, 42,
               45, 48, 50, 53, 55, 56}
    Output: 12, 16, 22
    """
    k, x, arr = 3, 20, [12, 16, 22, 30, 35, 39, 42, 45, 48, 50, 53, 55, 56]
    assert k_closest_elements(k, x, arr) == [12, 16, 22]


def test_find_kth_largest_elements_example_3():
    """
    Example 3:
    Input: K = 5, X = 49
       arr[] = {12, 16, 22, 30, 35, 39, 42,
               45, 48, 50, 53, 55, 56}
    Output: 45, 48, 50, 53, 55
    """
    k, x, arr = 5, 49, [12, 16, 22, 30, 35, 39, 42, 45, 48, 50, 53, 55, 56]
    assert k_closest_elements(k, x, arr) == [45, 48, 50, 53, 55]


def test_find_kth_largest_elements_example_4():
    """
    Example 4:
    Input: K = 4, X = 27
       arr[] = {12, 16, 22, 30, 35, 39, 42,
               45, 48, 50, 53, 55, 56}
    Output: 16, 22, 30, 35
    """
    k, x, arr = 4, 27, [12, 16, 22, 30, 35, 39, 42, 45, 48, 50, 53, 55, 56]
    assert k_closest_elements(k, x, arr) == [16, 22, 30, 35]
