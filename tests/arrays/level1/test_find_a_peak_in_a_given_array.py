"""
A file test the find_peak_element function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.arrays.level1.find_a_peak_in_a_given_array import find_peak_element


def test_find_peak_element_example_1() -> None:
    """
    Example 1:
    Input: array[]= {5, 10, 20, 15}
    Output: 20
    Explanation: The element 20 has neighbors 10 and 15, both of them are less
    than 20.
    """
    array = [5, 10, 20, 15]
    assert find_peak_element(array) == 20


def test_find_peak_element_example_2() -> None:
    """
    Example 2:
    Input: array[] = {10, 20, 15, 2, 23, 90, 67}
    Output: 20 or 90
    Explanation: The element 20 has neighbors 10 and 15, both of them are less
    than 20, similarly 90 has neighbors 23 and 67.
    """
    array = [10, 20, 15, 2, 23, 90, 67]
    assert find_peak_element(array) == 90
