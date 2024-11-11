"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/sort-array-according-order-defined-another-array/

Author: Nathan Lutala (nlutala)
"""


def sort_array(arr1: list[int], arr2: list[int]) -> list[int]:
    """
    Given two arrays arr1[] and arr2[] of size m and n, the task is to sort
    arr1[] such that the relative order among the elements matches the order
    in arr2[]. For elements not present in arr2[], append them at the end in
    sorted order.\n

    :param - arr (list of integers)\n
    :param - target (an integer)

    returns a sorted list of integers according to the order defined in arr2.
    """
    sorted_array = []
    arr2_copy = arr2

    for num in arr2_copy:
        while num in arr1:
            if num in arr1:
                sorted_array.append(num)
                arr1.remove(num)

    remaning_nums = [num for num in arr1 if num not in sorted_array]

    return sorted_array + sorted(remaning_nums)
