"""
A file tests the get_rainwater_collected function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.arrays.level3.trapping_rainwater import get_rainwater_collected


def test_get_rainwater_collected_example_1():
    """
    Example 1:
    Input: arr[] = {3, 0, 1, 0, 4, 0, 2}
    Output: 10
    Explanation: We trap 0 + 3 + 2 + 3 + 0 + 2 + 0 = 10 units
    """
    arr = [3, 0, 1, 0, 4, 0, 2]
    assert get_rainwater_collected(arr) == 10


def test_get_rainwater_collected_example_2():
    """
    Example 2:
    Input: arr[]   = {3, 0, 2, 0, 4}
    Output: 7
    Explanation: We trap 0 + 3 + 1 + 3 + 0 = 7 units.
    """
    arr = [3, 0, 2, 0, 4]
    assert get_rainwater_collected(arr) == 7


def test_get_rainwater_collected_example_3():
    """
    Example 3:
    Input: arr[] = {1, 2, 3, 4}
    Output: 0
    Explanation : We cannot trap water as there is no height bound on both sides
    """
    arr = [1, 2, 3, 4]
    assert get_rainwater_collected(arr) == 0


def test_get_rainwater_collected_example_4():
    """
    Example 4:
    Input: arr[] = {10, 9, 0, 5}
    Output: 5
    Explanation : We trap 0 + 0 + 5 + 0 = 5
    """
    arr = [10, 9, 0, 5]
    assert get_rainwater_collected(arr) == 5


# Custom tests
def test_get_rainwater_collected_example_5():
    """
    Example 5:
    Input: arr[] = {10, 9, 0, 5, 0, 1}
    Output: 5
    Explanation : We trap 0 + 0 + 5 + 1 + 0 = 6
    """
    arr = [10, 9, 0, 5, 0, 1]
    assert get_rainwater_collected(arr) == 6


def test_get_rainwater_collected_example_6():
    """
    Example 6:
    Input: arr[] = {1, 2, 3, 4, 0, 3, 0, 4}
    Output: 0
    Explanation : We trap 3 + 2 + 1 + 0 + 4 + 1 + 4 + 0 = 15
    """
    arr = [1, 2, 3, 4, 0, 3, 0, 4]
    assert get_rainwater_collected(arr) == 15


def test_get_rainwater_collected_example_7():
    """
    Example 7:
    Input: arr[]   = {3, 0, 2, 0, 4, 1, 0, 7, 4, 0, 3}
    Output: 7
    Explanation: We trap 0 + 3 + 1 + 3 + 0 + 4 + 3 + 4 + 0 + 0 + 3 + 0 = 21
    """
    arr = [3, 0, 2, 0, 4, 1, 0, 7, 4, 0, 3]
    assert get_rainwater_collected(arr) == 21
