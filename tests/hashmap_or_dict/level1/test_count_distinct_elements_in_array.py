"""
A file tests the count_distinct function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.hashmap_or_dict.level1.count_distinct_elements_in_array import (
    count_distinct,
)


def test_count_distinct_example_1():
    """
    Example 1
    Input: arr[] = {10, 20, 20, 10, 30, 10}
    Output: 3
    Explanation: There are three distinct elements 10, 20, and 30.
    """
    arr = [10, 20, 20, 10, 30, 10]
    assert count_distinct(arr) == 3


def test_count_distinct_example_2():
    """
    Example 2
    Input: arr[] = {10, 20, 20, 10, 20}
    Output: 2
    """
    arr = [10, 20, 20, 10, 20]
    assert count_distinct(arr) == 2
