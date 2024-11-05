"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/find-subarray-with-given-sum/

Author: Nathan Lutala (nlutala)
"""


def get_subarray_with_given_sum(arr: list[int], s: int) -> tuple[int, int] | int:
    """
    Given a 1-based indexing array arr[] of integers and an integer sum. You
    mainly need to return the left and right indexes(1-based indexing) of that
    subarray. In case of multiple subarrays, return the subarray indexes which
    come first on moving from left to right. If no such subarray exists return
    an array consisting of element -1.\n

    :param - arr (a list of integers)\n
    :param - sum (an integer)\n

    returns the indexes of the subarray which adds up to the sum, -1 if no subarray found.
    """
    window_length = 2

    while window_length <= len(arr):
        for i in range(len(arr) - window_length + 1):
            if sum(arr[i : i + window_length]) == s:
                return (i + 1, i + window_length)

        window_length += 1

    return -1
