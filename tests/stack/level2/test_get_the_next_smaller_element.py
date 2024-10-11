"""
A file tests the next_smaller_element function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.stack.level2.get_the_next_smaller_element import next_smaller_element


def test_next_smaller_element_example_1():
    """
    Example 1:
    Input:  arr[] = {1, 6, 4, 10, 2, 5}
    Output:         {_, 1, 1,  4, 1, 2}
    First element ('1') has no element on left side. For 6,
    there is only one smaller element on left side '1'.
    For 10, there are three smaller elements on left side (1,
    6 and 4), nearest among the three elements is 4.
    """
    arr = [1, 6, 4, 10, 2, 5]
    assert next_smaller_element(arr) == None


def test_next_smaller_element_example_2():
    """
    Example 2:
    Input:  arr[] = {1, 6, 4, 10, 2, 5}
    Output:         {_, 1, 1,  4, 1, 2}
    First element ('1') has no element on left side. For 6,
    there is only one smaller element on left side '1'.
    For 10, there are three smaller elements on left side (1,
    6 and 4), nearest among the three elements is 4.
    """
    arr = [6, 4, 10, 2, 5, 1]
    assert next_smaller_element(arr) == 4


def test_next_smaller_element_example_3():
    """
    Example 3:
    Input:  arr[] = {1, 6, 4, 10, 2, 5}
    Output:         {_, 1, 1,  4, 1, 2}
    First element ('1') has no element on left side. For 6,
    there is only one smaller element on left side '1'.
    For 10, there are three smaller elements on left side (1,
    6 and 4), nearest among the three elements is 4.
    """
    arr = [4, 10, 2, 5, 1, 6]
    assert next_smaller_element(arr) == 2


def test_next_smaller_element_example_4():
    """
    Example 4:
    Input:  arr[] = {1, 6, 4, 10, 2, 5}
    Output:         {_, 1, 1,  4, 1, 2}
    First element ('1') has no element on left side. For 6,
    there is only one smaller element on left side '1'.
    For 10, there are three smaller elements on left side (1,
    6 and 4), nearest among the three elements is 4.
    """
    arr = [10, 2, 5, 1, 6, 4]
    assert next_smaller_element(arr) == 2


def test_next_smaller_element_example_5():
    """
    Example 5:
    Input:  arr[] = {1, 6, 4, 10, 2, 5}
    Output:         {_, 1, 1,  4, 1, 2}
    First element ('1') has no element on left side. For 6,
    there is only one smaller element on left side '1'.
    For 10, there are three smaller elements on left side (1,
    6 and 4), nearest among the three elements is 4.
    """
    arr = [2, 5, 1, 6, 4, 10]
    assert next_smaller_element(arr) == 1
