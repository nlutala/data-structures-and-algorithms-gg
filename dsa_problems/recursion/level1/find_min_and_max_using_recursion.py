"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/recursive-programs-to-find-minimum-and-maximum-elements-of-array/

Author: Nathan Lutala (nlutala)
"""


def get_min_and_max(arr: list[int], length: int) -> list[int]:
    """
    Given an array of integers arr, find the minimum and maximum element of that array
    using recursion.\n

    :param - arr (a list of integers)\n
    :param - length (an integer denoting the size of the list arr)\n

    Returns a list of the minimum and maximum element of the array.
    """
    if length == 1:
        return [arr[0], arr[0]]
    elif length == 2:
        return sorted(arr)
    else:
        minimum = arr[0]
        maximum = arr[0]

        for a in arr:
            if a < minimum:
                minimum = a

            if a > maximum:
                maximum = a

        if arr[0] in {minimum, maximum}:
            arr.append(arr[0])

        return get_min_and_max(arr[1:], len(arr[1:]))
