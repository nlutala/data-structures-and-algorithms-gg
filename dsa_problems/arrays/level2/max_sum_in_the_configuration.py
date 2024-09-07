"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/maximum-sum-iarri-among-rotations-given-array/

Author: Nathan Lutala (nlutala)
"""


def max_sum_of_index_and_elem(arr: list[int]) -> int:
    """
    Given an array arr[] of n integers, find the maximum that maximizes the
    sum of the value of i*arr[i] where i varies from 0 to n-1.\n

    :param - array (list of integers)\n

    returns the maximum sum of i * arr[i] among all rotations of a given array.
    """
    arrays = []
    max_sum = 0

    for i in range(len(arr)):
        temp_array = arr[i+1:] + arr[0:i+1]
        arrays.append(temp_array)

    for array in arrays:
        current_sum = 0
        for i, elem in enumerate(array):
            current_sum += i * elem

        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum
