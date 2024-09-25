"""
A file test the reverse_string function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.recursion.level1.print_reversed_string_using_recursion import (
    reverse_string,
)


# My own custom tests
def test_reverse_string_example_1():
    """
    Example 1:
    Input: string = "string"
    Output: "gnirts"
    """
    string = "string"
    assert reverse_string(string) == "gnirts"


def test_reverse_string_example_2():
    """
    Example 2:
    Input: string = "hello world"
    Output: "dlrow olleh"
    """
    string = "hello world"
    assert reverse_string(string) == "dlrow olleh"
