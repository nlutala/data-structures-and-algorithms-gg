"""
A file tests the kth_smallest_element function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.heaps.level2.how_to_implement_priority_queue_heap_or_array import (
    kth_smallest_element,
)


def test_find_kth_largest_elements_example_1():
    """
    Example 1:
    Input:k = 3 and array =
        10, 20, 30, 40
        15, 25, 35, 45
        24, 29, 37, 48
        32, 33, 39, 50
    Output: 20
    Explanation: The 3rd smallest element is 20
    """
    k, arr = 3, [[10, 20, 30, 40], [15, 25, 35, 45], [24, 29, 37, 48], [32, 33, 39, 50]]
    assert kth_smallest_element(k, arr) == 20


def test_find_kth_largest_elements_example_2():
    """
    Example 2:
    Input:k = 7 and array =
        10, 20, 30, 40
        15, 25, 35, 45
        24, 29, 37, 48
        32, 33, 39, 50
    Output: 30
    Explanation: The 7th smallest element is 30
    """
    k, arr = 7, [[10, 20, 30, 40], [15, 25, 35, 45], [24, 29, 37, 48], [32, 33, 39, 50]]
    assert kth_smallest_element(k, arr) == 30
