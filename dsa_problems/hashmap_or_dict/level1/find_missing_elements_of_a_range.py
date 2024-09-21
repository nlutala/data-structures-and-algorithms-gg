"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/find-missing-elements-of-a-range/

Author: Nathan Lutala (nlutala)
"""


def missing_elem_in_range(arr: list[int], low: int, high: int) -> list[int]:
    """
    Given an array, arr[0..n-1] of distinct elements and a range [low, high],
    find all numbers that are in a range, but not the array. The missing
    elements should be printed in sorted order.\n

    :param - arr (list of integers)\n
    :param - low (integer of the lower end of the range)\n
    :param - high (integer of the higher end of the range)\n

    returns a list of missing numbers of a range.
    """
    missing_elems = []

    while low <= high:
        if low not in set(arr):
            missing_elems.append(low)

        low += 1

    return missing_elems
