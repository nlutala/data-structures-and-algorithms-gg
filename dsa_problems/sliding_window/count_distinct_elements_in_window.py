"""
A file to tackle the example coding interview question as found on the website below:
https://www.geeksforgeeks.org/count-distinct-elements-in-every-window-of-size-k/

Author: Nathan Lutala (nlutala)
"""


def count_distinct_elems(arr: list[int], k: int) -> int:
    """
    Given an array of size N and an integer K, return the count of distinct
    numbers in all windows of size K.\n

    :param - arr (list of integers)\n
    :param - k (integer, the size of the window)\n

    Return the number of distinct elements of each window of size k.
    """
    result = []

    for i in range(len(arr) - k + 1):
        window_set = list(set(arr[i:i+k]))
        result.append(len(window_set))

    return result
