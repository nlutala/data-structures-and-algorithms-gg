"""
A file tests the count_distinct_elems function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.sliding_window.count_distinct_elements_in_window import (
    count_distinct_elems,
)


def test_count_distinct_elems_example_1() -> None:
    """
    Example 1
    Input: arr[] = {1, 2, 1, 3, 4, 2, 3}, K = 4
    Output: 3 4 4 3
    Explanation: First window is {1, 2, 1, 3}, count of distinct numbers is 3
                 Second window is {2, 1, 3, 4} count of distinct numbers is 4
                 Third window is {1, 3, 4, 2} count of distinct numbers is 4
                 Fourth window is {3, 4, 2, 3} count of distinct numbers is 3
    """
    arr = [1, 2, 1, 3, 4, 2, 3]
    k = 4
    assert count_distinct_elems(arr, k) == [3, 4, 4, 3]


def test_count_distinct_elems_example_2() -> None:
    """
    Example 2
    Input: arr[] = {1, 2, 4, 4}, K = 2
    Output: 2 2 1
    Explanation: First window is {1, 2}, count of distinct numbers is 2
                 First window is {2, 4}, count of distinct numbers is 2
                 First window is {4, 4}, count of distinct numbers is 1
    """
    arr = [1, 2, 4, 4]
    k = 2
    assert count_distinct_elems(arr, k) == [2, 2, 1]
