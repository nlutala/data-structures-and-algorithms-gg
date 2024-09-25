"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/remove-duplicates-sorted-array/

Author: Nathan Lutala (nlutala)
"""


def remove_duplicates(arr: list[int]) -> list[int]:
    """
    Given a sorted array arr[] of size N, the task is to remove the duplicate elements
    from the array. We need keep order of the remaining distinct elements as it was in
    the original array.\n

    :param - arr (list of integers)\n

    returns the sorted list of arr where each element is distinct.
    """
    return sorted(list(set(arr)))
