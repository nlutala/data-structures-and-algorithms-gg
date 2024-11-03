"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/find-k-closest-elements-given-value/

Author: Nathan Lutala (nlutala)
"""


def k_closest_elements(k: int, x: int, arr: list[int]) -> list[int]:
    """
    Given a sorted array arr[] and a value X, find the k closest elements to X
    in arr[].\n

    :param - arr (a list of integers)\n

    Returns the k closest elements to x.
    """
    new_arr = [num for num in arr if num != x]
    distance = None
    k_elements = []

    for i in range(len(new_arr) - k):
        subarray = new_arr[i : i + k]

        if distance is None:
            distance = sum([abs(x - num) for num in subarray])
            k_elements = subarray
        else:
            if sum([abs(x - num) for num in subarray]) < distance:
                distance = sum([abs(x - num) for num in subarray])
                k_elements = subarray

    return k_elements
