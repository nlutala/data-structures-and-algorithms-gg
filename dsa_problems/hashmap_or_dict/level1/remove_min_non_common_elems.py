"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/remove-minimum-number-elements-no-common-element-exist-array/

Author: Nathan Lutala (nlutala)
"""


def no_common_elems(arr1: list[int], arr2: list[int]) -> int:
    """
    Given two arrays arr1[] and arr2[] consisting of n and m elements
    respectively. The task is to find the minimum number of elements to remove
    from each array such that intersection of both arrays becomes empty and
    both arrays become mutually exclusive.\n

    :param - arr1 (list of integers)\n
    :param - arr2 (list of integers)\n

    returns the minimum number of elements to remove from each array.
    """
    arr1_set = list(set(arr1))
    arr2_set = list(set(arr2))

    num_to_remove = 0

    for a in arr1_set:
        if a in arr2:
            num_to_remove += 1

    return num_to_remove
