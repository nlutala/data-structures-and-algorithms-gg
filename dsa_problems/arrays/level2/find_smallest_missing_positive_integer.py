"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/find-the-smallest-positive-number-missing-from-an-unsorted-array/

Author: Nathan Lutala (nlutala)
"""


def smallest_missing_positive_int(arr: list) -> int | None:
    """
    Given an unsorted array arr[] with both positive and negative elements, the task is
    to find the smallest positive number missing from the array.\n

    :param - arr (list)\n

    returns the smallest positive integer missing from the array.
    """
    # Range starts from 1 as 0 is an integer but it's neither positive or negative.
    missing_ints: list[int] = [i for i in range(1, max(arr)) if i not in set(arr)]
    return missing_ints[0]
