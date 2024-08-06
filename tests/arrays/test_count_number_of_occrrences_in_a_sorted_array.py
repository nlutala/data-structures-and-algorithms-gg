"""
A file tests the count_occurrences function

Author: Nathan Lutala (nlutala)
"""

from arrays.count_number_of_occurrences_in_a_sorted_array import count_occurrences


def test_count_occurences():
    """
    Input: X = 2, Arr[] = {1, 1, 2, 2, 2, 2, 3}
    Output: 4
    Explanation: 2 occurs 4 times in the given array.
    """
    arr = [1, 1, 2, 2, 2, 2, 3]
    x = 2

    assert count_occurrences(arr, x) == 4
