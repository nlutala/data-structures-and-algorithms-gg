"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/top-50-problems-on-hash-data-structure-asked-in-sde-interviews/

Author: Nathan Lutala (nlutala)
"""


def majority_element(arr: list[int]) -> int:
    """
    Given an array arr. Find the majority element in the array. If no majority exists,
    return -1. A majority element in an array is an element that appears strictly more
    than arr.size() / 2 times in the array.\n

    :param - arr (list of integers)\n

    returns the element that repeats the most in an array.
    """
    majority_threshold = len(arr) // 2
    arr_dict = {}

    for a in arr:
        if str(a) not in arr_dict.keys():
            arr_dict[str(a)] = arr.count(a)

    majority = -1
    count = 0

    for elem in arr_dict:
        if arr_dict.get(elem) > majority_threshold and arr_dict.get(elem) > count:
            majority = int(elem)

    return majority
