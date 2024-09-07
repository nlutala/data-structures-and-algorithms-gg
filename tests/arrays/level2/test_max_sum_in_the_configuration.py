"""
A file tests the max_sum_of_index_and_elem function

Author: Nathan Lutala (nlutala)
"""

from arrays.level2.max_sum_in_the_configuration import (
    max_sum_of_index_and_elem,
)


def test_max_sum_of_index_and_elem_example_1():
    """
    Input: arr[] = {8, 3, 1, 2}
    Output: 29
    Explanation: Lets look at all the rotations,
    {8, 3, 1, 2} = 8*0 + 3*1 + 1*2 + 2*3 = 11
    {3, 1, 2, 8} = 3*0 + 1*1 + 2*2 + 8*3 = 29
    {1, 2, 8, 3} = 1*0 + 2*1 + 8*2 + 3*3 = 27
    {2, 8, 3, 1} = 2*0 + 8*1 + 3*2 + 1*3 = 17
    """
    arr = [8, 3, 1, 2]

    assert max_sum_of_index_and_elem(arr) == 29


def test_max_sum_of_index_and_elem_example_2():
    """
    Input: arr[] = {3, 2, 1}
    Output: 7
    Explanation: Lets look at all the rotations,
    {3, 2, 1} = 3*0 + 2*1 + 1*2 = 4
    {2, 1, 3} = 2*0 + 1*1 + 3*2 = 7
    {1, 3, 2} = 1*0 + 3*1 + 2*2 = 7
    """
    arr = [3, 2, 1]

    assert max_sum_of_index_and_elem(arr) == 7
