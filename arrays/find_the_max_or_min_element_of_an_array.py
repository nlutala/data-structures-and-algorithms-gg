"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/program-find-minimum-maximum-element-array/

Author: Nathan Lutala (nlutala)
"""


def find_max_element(array: list) -> int:
    """
    Given an array, write functions to find the maximum element in it.

    :param - array (list)

    returns the max integer in the array
    """
    max_element = array[0]
    for i in range(1, len(array)):
        max_element = array[i] if array[i] > max_element else max_element
    return max_element


def find_min_element(array: list) -> int:
    """
    Given an array, write functions to find the minimum element in it.

    :param - array (list)

    returns the min integer in the array
    """
    min_element = array[0]
    for i in range(1, len(array)):
        min_element = array[i] if array[i] < min_element else min_element
    return min_element
