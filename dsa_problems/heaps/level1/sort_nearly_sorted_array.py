"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/nearly-sorted-algorithm/

Author: Nathan Lutala (nlutala)
"""


def sort_array(arr: list[int], k: int) -> list[int]:
    """
    Given an array of N elements, where each element is at most K away from
    its target position, devise an algorithm that sorts in O(N log K) time.\n

    :param - arr (list of integers)\n
    :param - k (an integer)\n

    Retuns the sorted version of the array arr.
    """
    sorted_arr = []

    for i in range(len(arr)):
        if sorted_arr == []:
            sorted_arr.append(arr[i])
        else:
            if sorted_arr[0] >= arr[i]:
                sorted_arr.insert(0, arr[i])
            elif sorted_arr[-1] < arr[i]:
                sorted_arr.append(arr[i])
            else:
                if sorted_arr[-2] >= arr[i]:
                    sorted_arr.insert(len(sorted_arr)-2, arr[i])
                else:
                    sorted_arr.insert(len(sorted_arr)-1, arr[i])

    return sorted_arr
