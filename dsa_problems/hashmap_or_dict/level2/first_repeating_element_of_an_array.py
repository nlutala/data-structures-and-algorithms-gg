"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/find-first-repeating-element-array-integers/

Author: Nathan Lutala (nlutala)
"""


def repeating_element(arr: list[int]) -> int:
    """
    Given an array of integers arr[], The task is to find the index of first
    repeating element in it i.e. the element that occurs more than once and
    whose index of the first occurrence is the smallest. \n

    :param - arr (list of integers)\n

    returns the first element that repeats in the array.
    """
    elems = []

    for a in arr:
        if a not in elems:
            elems.append(a)

    for e in elems:
        if arr.count(e) > 1:
            return e
