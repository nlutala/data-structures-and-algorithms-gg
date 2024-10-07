"""
A file tests the reverse_string function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.stack.level1.reverse_individual_words import reverse_string


def test_reverse_string_example_1():
    """
    Example 1:
    Input : Hello World
    Output : olleH dlroW
    """
    string = "Hello World"
    assert reverse_string(string) == "olleH dlroW"


def test_reverse_string_example_2():
    """
    Example 2:
    Input :  Geeks for Geeks
    Output : skeeG rof skeeG
    """
    string = "Geeks for Geeks"
    assert reverse_string(string) == "skeeG rof skeeG"
