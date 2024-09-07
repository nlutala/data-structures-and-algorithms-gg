"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/find-first-repeating-element-array-integers/

Author: Nathan Lutala (nlutala)
"""


def find_first_repeating_integer(arr: list[int]) -> int:
    """
    Given an array of integers arr[], The task is to find the index of first
    repeating element in it i.e. the element that occurs more than once and
    whose index of the first occurrence is the smallest.\n

    :param - arr (list)\n

    returns a the first integer that occurs multiple times in the array.
    """

    for i, num in enumerate(arr):
        if num in arr[i + 1:]:
            return num

    return None
