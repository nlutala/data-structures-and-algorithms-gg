"""
A file tests the min_num_of_platforms function

Author: Nathan Lutala (nlutala)
"""

from arrays.level2.minimum_platforms import min_num_of_platforms


def test_min_num_of_platforms_example_1():
    """
    Example 1:

    Input:
    arr[] = {9:00, 9:40, 9:50, 11:00, 15:00, 18:00},
    dep[] = {9:10, 12:00, 11:20, 11:30, 19:00, 20:00}

    Output: 3

    Explanation: There are at-most three trains at a time (time between 9:40
    to 12:00)
    """
    arr = ["9:00", "9:40", "9:50", "11:00", "15:00", "18:00"]
    dep = ["9:10", "12:00", "11:20", "11:30", "19:00", "20:00"]

    assert min_num_of_platforms(arr, dep)


def test_min_num_of_platforms_example_2():
    """
    Example 2:

    Input:
    arr[] = {9:00, 9:40},
    dep[] = {9:10, 12:00}

    Output: 1
    """
    arr = ["9:00", "9:40"]
    dep = ["9:10", "12:00"]

    assert min_num_of_platforms(arr, dep)
