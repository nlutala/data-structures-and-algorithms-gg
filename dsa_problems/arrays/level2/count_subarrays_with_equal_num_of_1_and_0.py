"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/count-subarrays-equal-number-1s-0s/

Author: Nathan Lutala (nlutala)
"""


def count_equal_num_of_1_and_0(arr: list[int]) -> int:
    """
    Given an array arr[] of size n containing 0 and 1 only. The problem is to
    count the subarrays having an equal number of 0’s and 1’s.\n

    :param - arr (list of integers)\n

    returns a the amount of subarrays where there are an equal number of 0s
    and 1s.
    """
    num_of_subarrays = 0
    length_of_subarray = 2

    while length_of_subarray <= len(arr):
        for i in range(len(arr)):
            if i + length_of_subarray > len(arr):
                break
            else:
                sub_array = arr[i:length_of_subarray]
                if sub_array.count(0) == sub_array.count(1):
                    num_of_subarrays += 1

        length_of_subarray += 2

    return num_of_subarrays
