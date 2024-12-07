"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/sort-array-wave-form-2/

Author: Nathan Lutala (nlutala)
"""


def get_wave_array(arr1: list) -> list[int]:
    """
    Given an unsorted array of integers, sort the array into a wave array.
    An array arr[0..n-1] is sorted in wave form if:
    arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] >= ...

    param - arr1 (list)\n

    returns a wave array.
    """
    sorted_arr1 = sorted(arr1)
    smaller = sorted_arr1[: len(sorted_arr1) // 2]
    bigger = sorted_arr1[len(sorted_arr1) // 2 :]

    result = []

    while len(result) != len(arr1):
        if bigger:
            result.append(bigger.pop(0))
        else:
            break

        if smaller:
            result.append(smaller.pop(0))

    if len(smaller) > 1:
        return []
    elif len(smaller) == 1:
        print(result + smaller)
        return result + smaller
    else:
        print(result)
        return result
