"""
A file tests the find_subarray_with_0_sum function

Author: Nathan Lutala (nlutala)
"""

from arrays.level2.subarray_with_zero_sum import is_subarray_with_0_sum


def test_is_subarray_with_0_example_1():
    """
    Example 1:
    Input: {4, 2, -3, 1, 6}
    Output: true
    Explanation: There is a subarray with zero sum from index 1 to 3.
    """
    arr = [4, 2, -3, 1, 6]

    assert is_subarray_with_0_sum(arr) is True


def test_is_subarray_with_0_example_2():
    """
    Example 2:
    Input: {4, 2, 0, 1, 6}
    Output: true
    Explanation: The third element is zero. A single element is also a
    sub-array.
    """
    arr = [4, 2, 0, 1, 6]

    assert is_subarray_with_0_sum(arr) is True


def test_is_subarray_with_0_example_3():
    """
    Example 3:
    Input: {-3, 2, 3, 1, 6}
    Output: false
    """
    arr = [-3, 2, 3, 1, 6]

    assert is_subarray_with_0_sum(arr) is False
