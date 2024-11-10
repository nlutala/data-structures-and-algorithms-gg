"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/find-duplicates-given-array-elements-not-limited-range/

Author: Nathan Lutala (nlutala)
"""


def get_duplicates(arr: list[int]) -> list[int] | None:
    """
    Given an array of n integers. The task is to find all elements that have
    more than one occurrences. The output should only one occurrence of a
    number irrespective of number of occurrences in the input array.

    :param - arr (list of integers)\n

    returns the duplicate integers in the arr, and None if there are no 
    duplicates.
    """
    arr_set = []

    for num in arr:
        if num not in arr_set:
            arr_set.append(num)

    duplicates = []

    for num in arr_set:
        if arr.count(num) > 1:
            duplicates.append(num)

    return duplicates if len(duplicates) > 0 else None
