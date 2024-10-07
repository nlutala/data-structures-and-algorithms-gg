"""
A file tests the majority_element function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.hashmap_or_dict.level2.find_the_majority_element_in_an_array import (
    majority_element,
)


def test_majority_element_example_1():
    """
    Example 1
    Input : arr[] = {1, 1, 2, 1, 3, 5, 1}
    Output : 1
    Explanation: Note that 1 appear 4 times which is more than  7 / 2 times
    """
    arr = [1, 1, 2, 1, 3, 5, 1]
    assert majority_element(arr) == 1


def test_majority_element_example_2():
    """
    Example 2
    Input : arr[] = {3, 3, 4, 2, 4, 4, 2, 4}
    Output :  -1
    Explanation: There is no element whose frequency is greater than the half of the
    size of the array size.
    """
    arr = [3, 3, 4, 2, 4, 4, 2, 4]
    assert majority_element(arr) == -1


def test_majority_element_example_3():
    """
    Example 3
    Input : arr[] = {3}
    Output : 3
    Explanation: Appears more than n/2 times
    """
    arr = [3]
    assert majority_element(arr) == 3
