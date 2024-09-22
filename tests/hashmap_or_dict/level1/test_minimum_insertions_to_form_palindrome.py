"""
A file tests the min_insertions function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.hashmap_or_dict.level1.minimum_insertions_to_form_palindrome import (
    min_insertions,
)


def test_min_insertions_example_1():
    """
    Example 1
    Input: geeksforgeeks
    Output: 2
    geeksforgeeks can be changed as to: geeksroforskeeg
    """
    string = "geeksforgeeks"
    assert min_insertions(string) == 2


def test_min_insertions_example_2():
    """
    Example 2
    Input : aabbc
    Output : 0
    aabbc can be changed to: abcba
    """
    string = "aabbc"
    assert min_insertions(string) == 0


# Extra tests I've added just to make sure
def test_min_insertinos_example_3():
    """
    Example 3
    Input : nathan
    Output : 2
    nathan can be changed to: nathhtan
    """
    string = "nathan"
    assert min_insertions(string) == 2


def test_min_insertinos_example_4():
    """
    Example 4
    Input : hannah
    Output : 0
    hannah is a palindrome
    """
    string = "hannah"
    assert min_insertions(string) == 0


def test_min_insertinos_example_5():
    """
    Example 5
    Input : car
    Output : 2
    car can be changed to: carac
    """
    string = "car"
    assert min_insertions(string) == 2
