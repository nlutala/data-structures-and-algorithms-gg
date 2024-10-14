"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/print-all-subarrays-with-0-sum/

Author: Nathan Lutala (nlutala)
"""


def subarrays_with_zero_sum(arr: list[int]) -> list[list[int]]:
    """
    Given an array arr[] of size n, the task is to print all subarrays in the array
    which has sum 0.\n

    :param - arr (list of integers)\n

    returns a list of subarrays which have a sum of 0.
    """
    subarrays = None

    for i in range(len(arr)):
        window_length = i + 2
        arrays = [
            [j, j + window_length - 1]
            for j in range(len(arr) - window_length + 1)
            if sum(arr[j : j + window_length]) == 0
        ]

        if subarrays is None:
            subarrays = arrays
        else:
            subarrays += arrays

    for s in subarrays:
        print(f"Subarray found from Index {s[0]} to {s[1]}")

    return subarrays
