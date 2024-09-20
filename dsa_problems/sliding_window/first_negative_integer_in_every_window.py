"""
A file to tackle the example coding interview question as found on the website below:
https://www.geeksforgeeks.org/first-negative-integer-every-window-size-k/

Author: Nathan Lutala (nlutala)
"""


def find_first_negative_ints(arr: list[int], k: int) -> int | str:
    """
    Given an array and a positive integer k, find the first negative integer
    for each window(contiguous subarray) of size k. If a window does not
    contain a negative integer, then print 0 for that window.\n

    :param - arr (list of integers)\n
    :param - k (integer, the size of the window)\n

    Return the first negative integer of each window of size k.
    """
    result = []

    for i in range(len(arr) - k + 1):
        window = arr[i:i+k]
        negative_nums = [w for w in window if w < 0]

        if len(negative_nums) > 0:
            result.append(negative_nums[0])
        else:
            result.append(0)

    return result
