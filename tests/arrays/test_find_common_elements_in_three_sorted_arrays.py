"""
A file tests the find_common_elements function

Author: Nathan Lutala (nlutala)
"""

from arrays.level2.find_common_elements_in_three_sorted_arrays import (
    find_common_elements,
)


def test_count_pairs_with_sum():
    """
    Example 1:
    Input: A[] = {1, 5, 10, 20, 30} , B[] = {5, 13, 15, 20}, C[] = {5, 20} 
    Output: 5 20
    Explanation: 5 and 20 are common in all the arrays.
    """
    a = [1, 5, 10, 20, 30]
    b = [5, 13, 15, 20]
    c = [5, 20]

    assert find_common_elements(a, b, c) == [5, 20]
