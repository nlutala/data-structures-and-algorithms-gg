"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/find-if-there-is-a-subarray-with-0-sum/

Author: Nathan Lutala (nlutala)
"""


def is_subarray_with_0_sum(arr: list[int]) -> bool:
    """
    Given an array of positive and negative numbers, the task is to find if
    there is a subarray (of size at least one) with 0 sum.\n

    :param - arr (list of integers)\n

    returns true or false if there is a subarray of (size at least one) with 0
    sum.
    """
    length_of_sub_array = 1

    while length_of_sub_array < len(arr) + 1:
        for i in range(len(arr)):
            if sum(arr[i:i + length_of_sub_array]) == 0:
                return True

        length_of_sub_array += 1

    return False
