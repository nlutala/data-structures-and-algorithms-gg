"""
A file that tests the sum_of_elements functions

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.heaps.level1.sum_of_all_elements_between import sum_of_elements


def test_sum_of_elements_example_1():
    """
    Example 1:
    Input : arr[] = {20, 8, 22, 4, 12, 10, 14},  k1 = 3,  k2 = 6
    Output : 26
         3rd smallest element is 10. 6th smallest element
         is 20. Sum of all element between k1 & k2 is
         12 + 14 = 26
    """
    arr = [20, 8, 22, 4, 12, 10, 14]
    k1 = 3
    k2 = 6
    assert sum_of_elements(arr, k1, k2) == 26


def test_sum_of_elements_example_2():
    """
    Example 2:
    Input : arr[] = {10, 2, 50, 12, 48, 13}, k1 = 2, k2 = 6
    Output : 73
    """
    arr = [10, 2, 50, 12, 48, 13]
    k1 = 2
    k2 = 6
    assert sum_of_elements(arr, k1, k2) == 73
