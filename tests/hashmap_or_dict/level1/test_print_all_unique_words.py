"""
A file tests the unique_words function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.hashmap_or_dict.level1.print_all_unique_words import (
    unique_words,
)


def test_unique_words_example_1():
    """
    Example 1:
    Input: Java is great. Grails is also great
    Output: Java
    Grails
    also
    """
    string = "Java is great. Grails is also great"
    assert unique_words(string) == ["Java", "Grails", "also"]


def test_unique_words_example_2():
    """
    Example 2:
    Input: "geeks for geeks"
    Output: "for"
    """
    string = "geeks for geeks"
    assert unique_words(string) == ["for"]
