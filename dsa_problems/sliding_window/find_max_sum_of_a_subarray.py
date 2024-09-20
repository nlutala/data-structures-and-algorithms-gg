"""
A file to tackle the example coding interview question as found on the website below:
https://www.geeksforgeeks.org/find-maximum-minimum-sum-subarray-size-k/

Author: Nathan Lutala (nlutala)
"""


def find_max_of_subarray(arr: list[int], k: int) -> int | str:
    """
    Given an array of integers and a number k, find the maximum sum of a subarray of
    size k.\n

    :param - arr (list of integers)\n
    :param - k (integer, the sum the subarray should add up to)\n

    Return the max sum of the subarray with a length of k
    """
    if k > len(arr):
        return "Invalid"
    else:
        max_sum = None

        for i in range(len(arr) - k + 1):
            if max_sum is None:
                max_sum = sum(arr[i : i + k])
            else:
                if sum(arr[i : i + k]) > max_sum:
                    max_sum = sum(arr[i : i + k])

        return max_sum
