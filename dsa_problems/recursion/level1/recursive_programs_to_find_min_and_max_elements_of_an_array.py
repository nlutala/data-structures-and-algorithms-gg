"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/recursive-programs-to-find-minimum-and-maximum-elements-of-array/

Author: Nathan Lutala (nlutala)
"""


def get_min_and_max(arr: list[int]) -> list[int]:
    """
    Given an array of integers arr, the task is to find the minimum and
    maximum element of that array using recursion.\n

    :param - arr (a list of integers)\n

    Returns the minimum and maximum element in the array.
    """
    if len(arr) <= 2:
        return sorted(arr)
    else:
        if arr[0] == min(arr) or arr[0] == max(arr):
            return get_min_and_max(arr[1:] + [arr[0]])

        return get_min_and_max(arr[1:])
