"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/quick-sort-algorithm/

Author: Nathan Lutala (nlutala)
"""


def quick_sort(arr: list) -> list[int]:
    """
    Given an array of n elements, return a sorted array using the quick sort
    algorithm.\n

    Note: The repeating element should be printed only once.\n

    :param - arr (list)\n

    returns the sorted array.
    """

    if len(arr) == 1:
        return arr
    elif len(arr) == 2:
        return [arr[1], arr[0]] if arr[0] >= arr[1] else [arr[0], arr[1]]
    else:

        def quick_sort_recurse(
                arr: list[int], left_part: list[int], right_part: list[int]
        ) -> list[int]:
            """
            :param - pivot (int)\n
            :param - arr (list of integers)\n
            :param - left_part (list of integers smaller than the pivot)\n
            :param - right_part (list of integers larger than the pivot)\n

            Returns a sorted list sorted by the pivot
            """

            if len(arr) == 0:
                return left_part + right_part
            else:
                pivot = arr[-1]
                new_left = [num for num in arr if num <= pivot]
                new_right = [num for num in arr if num > pivot]

                final_left = quick_sort_recurse(left_part, new_left, [])
                final_right = quick_sort_recurse(right_part, new_right, [])

            return final_left + final_right

        return quick_sort_recurse(arr, [], [])
