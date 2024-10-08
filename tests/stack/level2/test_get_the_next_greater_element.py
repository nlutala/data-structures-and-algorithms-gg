"""
A file tests the next_greater_element function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.stack.level2.get_the_next_greater_element import next_greater_element


def test_next_greater_element_example_1():
    """
    Example 1:
    Input: arr[] = [ 4 , 5 , 2 , 25 ]
    Output:  4      –>   5
               5      –>   25
               2      –>   25
              25     –>   -1
    Explanation: Except 25 every element has an element greater than them present on the
    right side
    """
    arr = [4, 5, 2, 25]
    assert next_greater_element(arr) == 5


def test_next_greater_element_example_2():
    """
    Example 2:
    Input: arr[] = [ 4 , 5 , 2 , 25 ]
    Output:  4      –>   5
               5      –>   25
               2      –>   25
              25     –>   -1
    Explanation: Except 25 every element has an element greater than them present on the
    right side
    """
    arr = [5, 2, 25, 4]
    assert next_greater_element(arr) == 25


def test_next_greater_element_example_3():
    """
    Example 3:
    Input: arr[] = [ 4 , 5 , 2 , 25 ]
    Output:  4      –>   5
               5      –>   25
               2      –>   25
              25     –>   -1
    Explanation: Except 25 every element has an element greater than them present on the
    right side
    """
    arr = [2, 25, 4, 5]
    assert next_greater_element(arr) == 25


def test_next_greater_element_example_4():
    """
    Example 4:
    Input: arr[] = [ 4 , 5 , 2 , 25 ]
    Output:  4      –>   5
               5      –>   25
               2      –>   25
              25     –>   -1
    Explanation: Except 25 every element has an element greater than them present on the
    right side
    """
    arr = [25, 4, 5, 2]
    assert next_greater_element(arr) == -1


def test_next_greater_element_example_5():
    """
    Example 5:
    Input: arr[] = [ 13 , 7, 6 , 12 ]
    Output:  13      –>    -1
                7       –>     12
                6       –>     12
               12      –>     -1
    Explanation: 13 and 12 don’t have any element greater than them present on the right
    side
    """
    arr = [13, 7, 6, 12]
    assert next_greater_element(arr) == -1


def test_next_greater_element_example_6():
    """
    Example 6:
    Input: arr[] = [ 13 , 7, 6 , 12 ]
    Output:  13      –>    -1
                7       –>     12
                6       –>     12
               12      –>     -1
    Explanation: 13 and 12 don’t have any element greater than them present on the right
    side
    """
    arr = [7, 6, 12, 13]
    assert next_greater_element(arr) == 12


def test_next_greater_element_example_7():
    """
    Example 7:
    Input: arr[] = [ 13 , 7, 6 , 12 ]
    Output:  13      –>    -1
                7       –>     12
                6       –>     12
               12      –>     -1
    Explanation: 13 and 12 don’t have any element greater than them present on the right
    side
    """
    arr = [6, 12, 13, 7]
    assert next_greater_element(arr) == 12


def test_next_greater_element_example_8():
    """
    Example 8:
    Input: arr[] = [ 13 , 7, 6 , 12 ]
    Output:  13      –>    -1
                7       –>     12
                6       –>     12
               12      –>     -1
    Explanation: 13 and 12 don’t have any element greater than them present on the right
    side
    """
    arr = [12, 13, 7, 6]
    assert next_greater_element(arr) == 13


def test_next_greater_element_example_9():
    """
    Example 9:
    Input: arr[] = [ 13 , 7, 6 , 12 ]
    Output:  13      –>    -1
                7       –>     12
                6       –>     12
               12      –>     -1
    Explanation: 13 and 12 don’t have any element greater than them present on the right
    side
    """
    arr = [13, 7, 6, 12]
    assert next_greater_element(arr) == -1
