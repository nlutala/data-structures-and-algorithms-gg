"""
A file tests the min_jumps function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.arrays.level2.min_number_of_jumps_to_end import min_jumps


def test_min_jumps_example_1():
    """
    Example 1:
    Input: arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}
    Output: 3 (1 -> 3 -> 9 -> 9)
    Explanation: Jump from 1st element to 2nd element as there is only 1 step.
    Now there are three options 5, 8 or 9. If 8 or 9 is chosen then the end
    node 9 can be reached. So 3 jumps are made.
    """
    arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]

    assert min_jumps(arr) == 3


def test_min_jumps_example_2():
    """
    Example 2:
    Input:  arr[] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1}
    Output: 10
    Explanation: In every step a jump is needed so the count of jumps is 10.
    """
    arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    assert min_jumps(arr) == 10


def test_min_jumps_example_3():
    """
    Example 3 (an example I made up):
    Input:  arr[] = {1, 2, 1, 3, 1, 9, 1, 1, 1, 1, 1}
    Output: 4
    Explanation: (1 -> 2, 2 -> 3, 3 -> 9, 9 -> end)
    """
    arr = [1, 2, 1, 3, 1, 9, 1, 1, 1, 1, 1]

    assert min_jumps(arr) == 4


def test_min_jumps_example_4():
    """
    Example 4 (another example I made up):
    Input:  arr[] = {12, 2, 1, 3, 1, 9, 1, 1, 1, 1, 1}
    Output: 1
    Explanation: Jump from the 1st element straight to the end.
    """
    arr = [12, 2, 1, 3, 1, 9, 1, 1, 1, 1, 1]

    assert min_jumps(arr) == 1


def test_min_jumps_example_5():
    """
    Example 5:
    Input:  arr[] = {1, 1, 1, 1}
    Output: 3
    Explanation: In every step a jump is needed so the count of jumps is 3.
    """
    arr = [1, 1, 1, 1]

    assert min_jumps(arr) == 3


def test_min_jumps_example_6():
    """
    Example 6:
    Input:  arr[] = {2, 2, 2, 2, 2}
    Output: 2
    """
    arr = [2, 2, 2, 2, 2]

    assert min_jumps(arr) == 2
