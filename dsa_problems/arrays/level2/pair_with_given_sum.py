"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/check-if-pair-with-given-sum-exists-in-array/

Author: Nathan Lutala (nlutala)
"""


def two_sum_exists(arr: list[int], target: int) -> bool:
    """
    Given an array arr[] of n integers and a target value, the task is to find whether
    there is a pair of elements in the array whose sum is equal to target. This problem
    is a variation of 2Sum problem.\n

    :param - arr (list of integers)\n
    :param - target (an integer)\n

    returns True if there are two numbers in the arr list which adds up to the target
    integer. False if otherwise.
    """

    for i in range(len(arr)):
        if target - arr[i] in arr[i + 1 :]:
            return True

    return False
