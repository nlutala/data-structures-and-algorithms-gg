"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/range-queries-for-frequencies-of-array-elements/

Author: Nathan Lutala (nlutala)
"""


def frequency_of_element_in_range(
    arr: list[int], left: int, right: int, element: int
) -> int:
    """
    Given an array of n non-negative integers. The task is to find frequency
    of a particular element in the arbitrary range of array[]. The range is
    given as positions (not 0 based indexes) in array. There can be multiple
    queries of given type.\n

    :param - arr (list of integers)\n
    :param - left (the start of the range)\n
    :param - right (the end of the range)\n
    :param - element (the number that you are looking for in said range)

    returns the amount of times the element is in the range.
    """
    arr_dict = {}

    for elem in arr[left - 1 : right]:
        if arr_dict.get(str(elem)) is None:
            arr_dict[str(elem)] = 1
        else:
            arr_dict[str(elem)] = arr_dict.get(str(elem)) + 1

    if arr_dict.get(str(element)) is None:
        return 0

    return arr_dict.get(str(element))
