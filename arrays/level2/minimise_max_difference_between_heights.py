"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/minimize-the-maximum-difference-between-the-heights/

Author: Nathan Lutala (nlutala)
"""


def min_max_difference(arr: list[str], k: int) -> int:
    """
    Given the heights of N towers and a value of K, Either increase or
    decrease the height of every tower by K (only once) where K > 0. After
    modifications, the task is to minimize the difference between the heights
    of the longest and the shortest tower and output its difference.\n

    :param - arr (list of heights as integers)\n
    :param - k (int)\n

    returns the difference between the longest and shortest tower.
    """
    pivot = min(arr) + k
    new_arr = []

    for elem in arr:
        if elem > pivot:
            new_arr.append(elem - k)
        else:
            new_arr.append(elem - k)

    return max(new_arr) - min(new_arr)
