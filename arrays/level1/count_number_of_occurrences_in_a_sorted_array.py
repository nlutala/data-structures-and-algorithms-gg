"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/count-number-of-occurrences-or-frequency-in-a-sorted-array/

Author: Nathan Lutala (nlutala)
"""


def count_occurrences(array: list, x: int) -> int:
    """
    Given a sorted array arr[] of size N and a number X, you need to find the
    number of occurrences of X in given array.

    :param - array (list)\n
    :param - x (int)\n

    returns the number of the number x in the array
    """
    occurrences = 0

    for number in array:
        occurrences = occurrences + 1 if number == x else occurrences

    return occurrences
