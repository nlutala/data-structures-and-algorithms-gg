"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/k-largestor-smallest-elements-in-an-array/

Author: Nathan Lutala (nlutala)
"""


def k_largest_elements(arr: list[int], k: int) -> list[int]:
    """
    Given an array arr[] of size N, the task is to printing K largest elements
    in an array.\n

    Note: Elements in output array can be in any order\n

    :param - arr (a list of integers)\n

    Returns k largest elements in the list arr.
    """
    elements = set()

    while len(list(elements)) < k:
        max_element = arr[0]
        index = 0

        for i in range(len(arr)):
            if max_element < arr[i]:
                max_element = arr[i]
                index = i

        elements.add(max_element)
        arr = arr[0:index] + arr[index + 1 :]

    return sorted(list(elements), reverse=True)
