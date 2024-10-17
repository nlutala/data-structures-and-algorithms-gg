"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/smallest-subarray-k-distinct-numbers/

Author: Nathan Lutala (nlutala)
"""


def smallest_subarray(arr: list[int], k: int) -> list[int] | str:
    """
    We are given an array consisting of n integers and an integer k. We need to find the
    minimum range in array [l, r] (both l and r are inclusive) such that there are
    exactly k different numbers. If such subarray doesn’t exist print “Invalid k”.\n

    :param - arr (list of integers)\n
    :param - k (an integer)

    returns the the minimum range in array [l, r] (both l and r are inclusive) or
    "Invalid k" if otherwise.
    """
    if len(list(set(arr))) < k:
        return "Invalid k"

    for i in range(len(arr) - k + 1):
        if len(list(set(arr[i : i + k]))) == k:
            return [i, i + k - 1]
