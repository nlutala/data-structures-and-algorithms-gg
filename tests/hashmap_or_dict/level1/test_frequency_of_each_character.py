"""
A file tests the char_frequency function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.hashmap_or_dict.level1.frequency_of_each_character import (
    char_frequency,
)


def test_char_frequency_example_1():
    """
    Example 1:
    Input: str = "geeksforgeeks"
    Output:
    r 1
    e 4
    s 2
    g 2
    k 2
    f 1
    o 1
    """
    string = "geeksforgeeks"

    assert char_frequency(string) == [
        ["g", 2],
        ["e", 4],
        ["k", 2],
        ["s", 2],
        ["f", 1],
        ["o", 1],
        ["r", 1],
    ]


def test_char_frequency_example_2():
    """
    Example 2:
    Input: str = "programming"
    Output:
    n 1
    i 1
    p 1
    o 1
    r 2
    a 1
    g 2
    m 2
    """
    string = "programming"

    assert char_frequency(string) == [
        ["p", 1],
        ["r", 2],
        ["o", 1],
        ["g", 2],
        ["a", 1],
        ["m", 2],
        ["i", 1],
        ["n", 1]
    ]
