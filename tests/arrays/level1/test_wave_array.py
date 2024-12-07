"""
A file tests the get_wave_array function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.arrays.level1.wave_array import get_wave_array


def test_get_wave_array_1():
    """
    Example 1:
    Input:  arr[] = {10, 5, 6, 3, 2, 20, 100, 80}
    Output: arr[] = {10, 5, 6, 2, 20, 3, 100, 80}
    Explanation:
    here you can see {10, 5, 6, 2, 20, 3, 100, 80} first element is larger
    than the second and the same thing is repeated again and again. large
    element – small element-large element -small element and so on .it can be
    small element-larger element – small element-large element -small element
    too. all you need to maintain is the up-down fashion which represents a
    wave. there can be multiple answers.
    """
    arr1 = [10, 5, 6, 3, 2, 20, 100, 80]
    assert get_wave_array(arr1) in [
        [10, 5, 6, 2, 20, 3, 100, 80],
        [10, 5, 6, 3, 20, 2, 100, 80],
        [10, 6, 20, 5, 80, 3, 100, 2],
        [10, 2, 20, 3, 80, 5, 100, 6],
    ]


def test_get_wave_array_2():
    """
    Example 2:
    Input: arr[] = {20, 10, 8, 6, 4, 2}
    Output: arr[] = {20, 8, 10, 4, 6, 2}
    """
    arr1 = [20, 10, 8, 6, 4, 2]
    assert get_wave_array(arr1) in [[20, 8, 10, 4, 6, 2], [8, 2, 10, 4, 20, 6]]


# Custom test
def test_get_wave_array_3():
    """
    Example 3:
    Input: arr[] = {20, 10, 8, 6, 4, 2, 100}
    Output: arr[] = {20, 8, 10, 4, 6, 2, 100}
    """
    arr1 = [20, 8, 10, 4, 6, 2, 100]
    assert get_wave_array(arr1) in [
        [20, 8, 10, 4, 6, 2, 100],
        [8, 2, 10, 4, 20, 6, 100],
    ]


def test_get_wave_array_4():
    """
    Example 3:
    Input: arr[] = {20, 10, 8, 6, 4, 2, 1, 100}
    Output: arr[] = {20, 8, 10, 4, 6, 2, 100, 1}
    """
    arr1 = [20, 10, 8, 6, 4, 2, 1, 100]
    assert get_wave_array(arr1) in [[8, 1, 10, 2, 20, 4, 100, 6]]
