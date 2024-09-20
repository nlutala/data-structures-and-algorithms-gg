"""
A file to tackle the example coding interview question as found on the website below:
https://www.geeksforgeeks.org/longest-sub-array-sum-k/

Author: Nathan Lutala (nlutala)
"""


def longest_subarray(arr: list[int], k: int) -> int:
    """
    Given an array arr[] of size n containing integers. The problem is to find the
    length of the longest sub-array having sum equal to the given value k.\n

    :param - arr (list of integers)\n
    :param - k (integer, the sum the subarray should add up to)

    Return the maximum sum of the subarray with a length of k
    """
    if sum(arr) == k:
        return len(arr)
    else:
        window_len = len(arr) - 1

        while window_len > 0:
            for i in range(len(arr) - window_len):
                if sum(arr[i : i + window_len]) == k:
                    return len(arr[i : i + window_len])

            window_len -= 1

        return window_len
