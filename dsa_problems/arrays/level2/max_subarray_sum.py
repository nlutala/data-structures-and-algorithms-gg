"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/

Author: Nathan Lutala (nlutala)
"""


def get_max_subarray_sum(arr: list[int]) -> int:
    """
    Given an array arr[] of size N. The task is to find the sum of the
    contiguous subarray within a arr[] with the largest sum.\n

    :param - arr (list of integers)\n

    returns the sum of the subarray with the maximum sum.
    """
    # Edge case of if all the integers in the array are positive
    positive_nums = [num for num in arr if num >= 0]
    if len(arr) == len(positive_nums):
        return sum(arr)
    else:
        length_of_subarray = 1
        max_subarray_sum = 0

        while length_of_subarray < len(arr) + 1:
            for i in range(len(arr)):
                if sum(arr[i:i + length_of_subarray]) > max_subarray_sum:
                    max_subarray_sum = sum(arr[i:i + length_of_subarray])

            length_of_subarray += 1

        return max_subarray_sum
