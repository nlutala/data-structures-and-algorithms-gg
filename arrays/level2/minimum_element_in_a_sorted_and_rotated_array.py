"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/find-minimum-element-in-a-sorted-and-rotated-array/

Author: Nathan Lutala (nlutala)
"""


def min_elem(array: list[int]) -> int:
    """
    Given a sorted array arr[] (may be distinct or may contain duplicates) of
    size N that is rotated at some unknown point, the task is to find the
    minimum element in it.\n

    :param - array (list of integers)\n

    returns the smallest number in the array.
    """
    smallest_number = array[0]

    for num in array:
        if num < smallest_number:
            smallest_number = num

    return smallest_number
