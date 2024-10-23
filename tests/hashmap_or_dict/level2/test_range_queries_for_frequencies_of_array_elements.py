"""
A file tests the frequency_of_element_in_range function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.hashmap_or_dict.level2.range_queries_for_frequencies_of_array_elements import (
    frequency_of_element_in_range,
)


def test_frequency_of_element_in_range_example_1():
    """
    Example 1
    Input: arr[] = {2, 8, 6, 9, 8, 6, 8, 2, 11}, left = 2, right = 8,
           element = 8
    Output: 3
    Explanation: The element 8 appears 3 times in arr[left-1..right-1]
    """
    arr, left, right, element = [2, 8, 6, 9, 8, 6, 8, 2, 11], 2, 8, 8
    assert frequency_of_element_in_range(arr, left, right, element) == 3


def test_frequency_of_element_in_range_example_2():
    """
    Example 2
    Input: arr[] = {2, 8, 6, 9, 8, 6, 8, 2, 11}, left = 2, right = 5,
           element = 6
    Output: 3
    Explanation: The element 8 appears 3 times in arr[left-1..right-1]
    """
    arr, left, right, element = [2, 8, 6, 9, 8, 6, 8, 2, 11], 2, 5, 6
    assert frequency_of_element_in_range(arr, left, right, element) == 1
