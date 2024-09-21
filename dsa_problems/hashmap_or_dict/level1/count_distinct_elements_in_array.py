"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/count-distinct-elements-in-an-array/

Author: Nathan Lutala (nlutala)
"""


def count_distinct(arr: list[int]) -> int:
    """
    Given an array arr[] of length N, The task is to count all distinct
    elements in arr[].\n

    :param - arr (list of integers)\n

    returns a the number of distinct elements in the array.
    """

    # You can do this in 2 ways
    # Method 1
    """
    freq = {}

    for i in range(len(arr)):
        if freq.get(str(arr[i])) is None:
            freq[str(arr[i])] = 1
        else:
            freq[str(arr[i])] = freq.get(str(arr[i])) + 1

    return len(freq)
    """

    # Method 2 (my preferred method)
    return len(list(set(arr)))
