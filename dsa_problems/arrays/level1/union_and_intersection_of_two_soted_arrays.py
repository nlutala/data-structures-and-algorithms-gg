"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/union-and-intersection-of-two-sorted-arrays-2/

Author: Nathan Lutala (nlutala)
"""


def union_and_intersection(arr1: list, arr2: list) -> list[int]:
    """
    Given two sorted arrays, find their union and intersection.

    :param - arr1 (list)\n
    :param - arr2 (list)\n

    returns two lists with the union and intersection (respectively).
    """
    # Calculate union
    union = list(set(sorted(arr1 + arr2)))

    # Calculate intersection
    intersection = [u for u in union if u in arr1 and u in arr2]

    return union, intersection
