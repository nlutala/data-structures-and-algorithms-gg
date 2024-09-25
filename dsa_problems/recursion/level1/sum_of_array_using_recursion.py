"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/sum-array-elements-using-recursion/

Author: Nathan Lutala (nlutala)
"""


def array_sum(arr: list[int]) -> int:
    """
    Given an array of integers, find sum of array elements using recursion.\n

    :param - arr (a list of integers)\n

    Return the sum of arr.
    """
    if len(arr) == 1:
        return arr.pop()
    else:
        return arr.pop() + array_sum(arr)
