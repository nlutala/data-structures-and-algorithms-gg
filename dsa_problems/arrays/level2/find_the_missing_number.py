"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/find-the-missing-number/

Author: Nathan Lutala (nlutala)
"""


def find_missing_number(arr: list) -> int:
    """
    Given an array arr[] of size N-1 with integers in the range of [1, N], the
    task is to find the missing number from the first N integers. \n

    Note: There are no duplicates in the list.

    :param - arr (list)\n

    returns the missing number in the array.
    """
    new_array = sorted(arr.copy())
    prev_num = new_array[0]

    for i in range(1, len(new_array)):
        if prev_num + 1 != new_array[i]:
            return prev_num + 1
        else:
            prev_num = new_array[i]

    return -1  # Just in case there isn't a missing number
