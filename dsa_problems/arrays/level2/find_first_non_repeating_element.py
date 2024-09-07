"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/non-repeating-element/

Author: Nathan Lutala (nlutala)
"""


def find_non_repeating_integer(arr: list[int]) -> int:
    """
    Given an array of integers of size N, the task is to find the first
    non-repeating element in this array.\n

    :param - arr (list)\n

    returns a the first integer that doesn't repeat in the array.
    """
    for i, num in enumerate(arr):
        if num not in arr[i + 1:] and num not in arr[:i]:
            return num

    return None
