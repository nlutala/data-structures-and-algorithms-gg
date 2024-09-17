"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/

Author: Nathan Lutala (nlutala)
"""


def max_of_subarray(arr: list[int], k: int) -> list[int]:
    """
    Given an array and an integer K, find the maximum for each and every contiguous
    subarray of size K.\n

    :param - arr (the list of integer numbers)\n
    :param - k (an integer denoting how long each subarray should be)

    Return a list of the maximum for each and every contiguous subarray of size K.
    """
    if k == 1:
        return arr
    else:
        subarray_maxes = []

        for i in range(0, len(arr) - k + 1):
            subarray_maxes.append(max(arr[i : i + k]))

        return subarray_maxes
