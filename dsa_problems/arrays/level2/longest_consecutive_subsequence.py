"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/longest-consecutive-subsequence/

Author: Nathan Lutala (nlutala)
"""


def longest_sequence(array: list[int]) -> int:
    """
    Given an array of integers, find the length of the longest sub-sequence
    such that elements in the subsequence are consecutive integers, the
    consecutive numbers can be in any order.\n

    :param - array (list of integers)\n

    returns the amount of numbers that can be ordered into a consecutive
    sequence.
    """
    # Order elements in ascending order
    sorted_array = sorted(array)

    # Loop through the elements in the list to keep track of consecutive
    # numbers
    max_length_sequence = 1
    length_sequence = 1

    for i in range(1, len(sorted_array)):
        if sorted_array[i] == sorted_array[i - 1] + 1:
            length_sequence += 1
        else:
            if max_length_sequence < length_sequence:
                max_length_sequence = length_sequence

            length_sequence = 1

    return max_length_sequence
