"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/find-a-peak-in-a-given-array/
"""


def find_peak_element(array: list) -> int:
    """
    Given an array arr of n elements that is first strictly increasing and then
    maybe strictly decreasing, find the maximum element in the array.

    Note: If the array is increasing then just print the last element will be
    the maximum value.

    :param - array (list)

    returns the integer in the array
    """
    # Corner cases
    if array == sorted(array):
        """
        If the input array is sorted in a strictly increasing order, the
        last element is always a peak element.
        """
        return array[-1]
    elif array == sorted(array, reverse=True):
        """
        If the input array is sorted in a strictly decreasing order, the
        first element is always a peak element.
        """
        return array[0]
    elif [array[0] for i in range(len(array))] == array:
        """
        If all elements of the input array are the same, every element is a
        peak element.
        """
        return array[0]
    else:
        working_array = array
        while working_array:
            if working_array[0] > working_array[1]:
                return working_array[0]
            elif working_array[-2] > working_array[-1]:
                return working_array[-2]
            else:
                working_array = working_array[1:len(working_array)-1]
