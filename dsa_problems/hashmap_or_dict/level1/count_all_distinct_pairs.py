"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/count-pairs-difference-equal-k/

Author: Nathan Lutala (nlutala)
"""


def count_sum_pairs(arr: list[int], k: int) -> int:
    """
    Given an integer array and a positive integer k, count all distinct pairs
    with differences equal to k.\n

    :param - arr (list of integers)\n
    :param - k (a positive integer, the target difference of the pairs).\n

    returns a the number of distinct pairs which equal k when subtracted.
    """
    pairs = set()

    for a in arr:
        if k + a in arr:
            if k + a < a:
                pairs.add((a, k + a))
            else:
                pairs.add((k + a, a))

    return len(list(pairs))
