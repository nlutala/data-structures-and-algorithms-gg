"""
A file tests the union_and_intersection function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.hashmap_or_dict.level1.find_union_and_intersection import (
    union_and_intersection,
)


def test_union_and_intersection():
    """
    Input : arr1[] = {7, 1, 5, 2, 3, 6}, arr2[] = {3, 8, 6, 20, 7}
    Output : Union : {1, 2, 3, 5, 6, 7, 8, 20}
    Intersection : {3, 6, 7}
    """
    arr1 = [7, 1, 5, 2, 3, 6]
    arr2 = [3, 8, 6, 20, 7]

    assert union_and_intersection(arr1, arr2) == [
        [1, 2, 3, 5, 6, 7, 8, 20],
        [3, 6, 7],
    ]
