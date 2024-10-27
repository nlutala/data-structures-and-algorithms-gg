"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/chocolate-distribution-problem/

Author: Nathan Lutala (nlutala)
"""


def distribute_chocolate(arr: list[int], m: int) -> int:
    """
    Given an array arr[] of n integers where arr[i] represents the number of
    chocolates in ith packet. Each packet can have a variable number of
    chocolates. There are m students, the task is to distribute chocolate
    packets such that:\n

    - Each student gets exactly one packet.\n
    - The difference between the maximum and minimum number of chocolates in
      the packets given to the students is minimized.\n

    :param - arr (list of integers)\n
    :param - m (an integer)

    returns the difference between the maximum and minimum number of choclates
    in the packets given to the students.
    """
    # Sort the arr in ascending order
    new_arr = sorted(arr)

    # Distribute the first m chocolates in new_arr
    distributed_chocolates = new_arr[0:m]

    # Return the max - min in the distributed chocolates
    return max(distributed_chocolates) - min(distributed_chocolates)
