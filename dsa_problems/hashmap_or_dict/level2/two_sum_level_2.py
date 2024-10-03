"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/print-all-pairs-with-given-sum/

Author: Nathan Lutala (nlutala)
"""


def two_sum(arr: list[int], target: int) -> list[list[int]]:
    """
    Given an array arr[] of size n and an integer target, the task is to find
    all distinct pairs in the array whose sum is equal to target. We can
    return pairs in any order, but all the returned pairs should be internally
    sorted, i.e., for any pair [q1, q2] the following should follow: q1 <= q2.
    \n

    :param - arr (list of integers)\n
    :param - target (an integer)

    returns a the longest consecutive subsequence that can be found in the
    array.
    """
    sums = []

    for a in arr:
        if target - a in arr and sorted([a, target - a]) not in sums:
            sums.append(sorted([a, target - a]))

    return sums
