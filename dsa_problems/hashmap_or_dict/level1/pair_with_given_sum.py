"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/check-if-pair-with-given-sum-exists-in-array/

Author: Nathan Lutala (nlutala)
"""


def two_sum(arr: list[int], target: int) -> bool:
    """
    Given an array arr[] of n integers and a target value, the task is to find
    whether there is a pair of elements in the array whose sum is equal to
    target. This problem is a variation of 2Sum problem.\n

    :param - arr (list of integers)\n
    :param - target (what two integers must add up to)\n

    returns True if a pair of elements in the array whose sum is equal to
    target and False if otherwise.
    """
    for i in range(len(arr)):
        # Get the arr without current element (arr[i])
        temp_arr = arr[:i] + arr[i + 1 :]

        if target - arr[i] in set(temp_arr):
            return True

    return False
