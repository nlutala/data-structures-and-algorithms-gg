"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/find-whether-an-array-is-subset-of-another-array-set-1/

Author: Nathan Lutala (nlutala)
"""


def is_subset(arr1: list[int], arr2: list[int]) -> str:
    """
    Given two arrays arr1[] and arr2[] of size m and n respectively, the task is to
    determine whether arr2[] is a subset of arr1[]. Both arrays are not sorted, and
    elements are distinct.\n

    :param - arr1 (list of integers)\n
    :param - arr2 (list of integers)\n

    returns "Yes" if arr2 is a subset of arr1 and "No" if otherwise.
    """
    subset = [num for num in arr2 if num in arr1]
    return "Yes" if subset == arr2 else "No"
