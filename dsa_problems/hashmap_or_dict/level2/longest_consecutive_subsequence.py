"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/longest-consecutive-subsequence/

Author: Nathan Lutala (nlutala)
"""


def consecutive_subsequence_len(arr: list[int]) -> int:
    """
    Given an array of integers, find the length of the longest sub-sequence such that
    elements in the subsequence are consecutive integers, the consecutive numbers can be
    in any order.\n

    :param - arr (list of integers)\n

    returns a the longest consecutive subsequence that can be found in the array.
    """
    # Remove duplicate elements and sort the list in ascending order
    sorted_arr: list[int] = sorted(list(set(arr)))

    # Create two variables to keep track of the length of the subsequnce
    length_of_sequence = 1
    current_length = 1

    for i in range(1, len(sorted_arr)):
        if sorted_arr[i] == sorted_arr[i - 1] + 1:
            current_length += 1
        else:
            # Only update length_of_current_sequence of the length of the current
            # subsequence (current_length) is greater
            if current_length > length_of_sequence:
                length_of_sequence = current_length
                current_length = 0

    return length_of_sequence
