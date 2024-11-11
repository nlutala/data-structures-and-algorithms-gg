"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/kth-smallest-element-in-a-row-wise-and-column-wise-sorted-2d-array/

Author: Nathan Lutala (nlutala)
"""


def kth_smallest_element(k: int, arr: list[int]) -> int:
    """
    Given an n x n matrix, where every row and column is sorted in non-decreasing order.
    Find the kth smallest element in the given 2D array.\n

    :param - k (an integer)\n
    :param - arr (a list of integers)\n

    Returns the kth smallest elements.
    """
    # Done but not in the way the question wants you to.
    new_arr = []
    for a in arr:
        new_arr += a

    return sorted(new_arr)[k - 1]
