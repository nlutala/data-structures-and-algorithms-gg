"""
A file tests the count_substring function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.hashmap_or_dict.level1.count_number_of_distinct_substring import (
    count_substring,
)


def test_count_substring_example_1():
    """
    Example 1
    Input : abcd
    Output : 10 (abcd abc ab a bcd bc b cd c d)
    All Elements are Distinct
    """
    string = "abcd"
    assert count_substring(string) == 10


def test_count_substring_example_2():
    """
    Example 2
    Input : aaa
    Output : 0 (aaa aa a aa a a)
    All elements are not Distinct
    """
    string = "aaa"
    assert count_substring(string) == 1


# Example test case I added myself
def test_count_substring_example_3():
    """
    Example 3
    Input : abaac
    Output : 6 (a, b, c, ab, ba, ac)
    """
    string = "abaac"
    assert count_substring(string) == 6
