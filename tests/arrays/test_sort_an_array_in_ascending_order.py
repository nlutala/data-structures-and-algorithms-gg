"""
A file test the sort_array_asc function

Author: Nathan Lutala (nlutala)
"""
from arrays.sort_an_array_in_ascending_order import sort_array_asc


def test_sort_array_asc():
    """
    Example 1:
    Input: original_array[] = {0, 23, 14, 12, 9}
    Output: sorted_array[] = {0, 9, 12, 14, 23}
    """
    original_array = [0, 23, 14, 12, 9]
    
    # What is baffling me is that the assertion commented below
    # doesn't work. Any reason why?
    # assert sort_array_asc(original_array) == sorted(original_array)
    assert sort_array_asc(original_array) == [0, 9, 12, 14, 23]
