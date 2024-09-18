"""
A file that tests the frequent_elements functions

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.heaps.top_k_frequent_elements import frequent_elements


def test_frequent_elements_example_1():
    """
    Example 1:
    Input: arr[] = {3, 1, 4, 4, 5, 2, 6, 1}, K = 2
    Output: 4 1
    Explanation: Frequency of 4 = 2, Frequency of 1 = 2.
    These two have the maximum frequency and 4 is larger than 1.
    """
    arr = [3, 1, 4, 4, 5, 2, 6, 1]
    k = 2
    assert frequent_elements(arr, k) == [4, 1]


def test_frequent_elements_example_2():
    """
    Example 2:
    Input: arr[] = {7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9}, K = 4
    Output: 5 11 7 10
    Explanation:
    Frequency of 5 = 3, 
    Frequency of 11 = 2, 
    Frequency of 7 = 2, 
    Frequency of 10 = 1
    These four have the maximum frequency and 5 is largest among rest.
    """
    arr = [7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9]
    k = 4
    assert frequent_elements(arr, k) == [5, 11, 7, 10]
