"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/program-to-reverse-an-array/
"""


def reverse_array(array: list) -> list:
    """
    Given an array (or string), the task is to reverse the array/string.

    :param - array (list)

    returns the reversed array
    """
    return [array[i] for i in range(len(array)-1, -1, -1)]
