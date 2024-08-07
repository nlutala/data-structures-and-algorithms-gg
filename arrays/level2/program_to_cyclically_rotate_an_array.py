"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/c-program-cyclically-rotate-array-one/

Author: Nathan Lutala (nlutala)
"""


def cyclically_rotate_array(arr: list) -> list[int]:
    """
    Given an array, the task is to cyclically rotate the array clockwise by
    one time.

    :param - arr1 (list)\n

    returns a new list with the rotated array.
    """
    new_arr = arr.copy()
    new_arr.insert(0, new_arr.pop(len(new_arr) - 1))
    return new_arr
