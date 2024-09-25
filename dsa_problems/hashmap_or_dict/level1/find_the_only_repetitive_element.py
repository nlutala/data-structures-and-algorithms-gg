"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/find-repetitive-element-1-n-1/

Author: Nathan Lutala (nlutala)
"""


def find_repeated_element(arr: list[int]) -> int:
    """
    Given an array of size N filled with numbers from 1 to N-1 in random order. The
    array has only one repetitive element. The task is to find the repetitive element.\n

    :param - arr (list of integers)\n

    returns the repeating number in the array.
    """
    for a in list(set(arr)):
        if arr.count(a) > 1:
            return a

    return None
