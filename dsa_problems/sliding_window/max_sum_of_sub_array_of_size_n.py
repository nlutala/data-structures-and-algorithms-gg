"""
A file to tackle the example coding interview question as found on the website below:
https://www.geeksforgeeks.org/window-sliding-technique/

Author: Nathan Lutala (nlutala)
"""


def max_sum_of_subarray(arr: list[int], k: int) -> int:
    """
    Given an array of size n and also an integer k, calculate the maximum sum of a
    subarray having size exactly k.\n

    :param - arr (list of integers)\n

    Return the maximum sum of the subarray with a length of k
    """
    max_sum = 0

    for i in range(0, len(arr) - 3):
        if arr[i] + arr[i + 1] + arr[i + 2] > max_sum:
            max_sum = arr[i] + arr[i + 1] + arr[i + 2]

    return max_sum
