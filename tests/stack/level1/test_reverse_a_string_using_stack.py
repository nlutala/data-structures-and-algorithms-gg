"""
A file tests the parenthesis_checker function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.stack.level1.reverse_a_string_using_stack import reverse_string


def test_reverse_string_example_1():
    """
    Example 1:
    Input: str = “GeeksQuiz”
    Output: ziuQskeeG
    """
    string = "GeeksQuiz"
    assert reverse_string(string) == "ziuQskeeG"


def test_reverse_string_example_2():
    """
    Example 2:
    Input: str = “abc”
    Output: cba
    """
    string = "abc"
    assert reverse_string(string) == "cba"
