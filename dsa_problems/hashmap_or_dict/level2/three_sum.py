"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/unique-triplets-sum-given-value/

Author: Nathan Lutala (nlutala)
"""


def get_three_sum(arr: list[int], target: int) -> list[list[int]]:
    """
    Given an array arr[], and an integer target, find all possible unique
    triplets in the array whose sum is equal to the given target value. We can
    return triplets in any order, but all the returned triplets should be
    internally sorted, i.e., for any triplet [q1, q2, q3], the condition
    q1 ≤ q2 ≤ q3 should hold.\n

    :param - arr (list of integers)\n
    :param - target (an integer)

    returns the triplets which add up to the target value.
    """
    sums = []
    sorted_arr = sorted(arr)
    used = []

    while len(sorted_arr) > 3:
        if sorted_arr[-1] + sorted_arr[-2] < target:
            if target - (sorted_arr[-1] + sorted_arr[-2]) in sorted_arr:
                number = target - (sorted_arr[-1] + sorted_arr[-2])
                sums.append(sorted([sorted_arr[-1], sorted_arr[-2], number]))
                used += sorted([sorted_arr[-1], sorted_arr[-2], number])

    return sums
