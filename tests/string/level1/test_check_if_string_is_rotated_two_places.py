"""
A file tests the is_rotated_two_places function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.string.level1.check_if_string_is_rotated_two_places import (
    is_rotated_two_places,
)


def test_is_rotated_two_places_example_1():
    """
    Example 1:
    Input: str1 = “amazon”, str2 = “azonam”
    Output: Yes
    Explanation: Rotating string1 by 2 places in anti-clockwise gives the string2.
    """
    str1 = "amazon"
    str2 = "azonam"
    assert is_rotated_two_places(str1, str2) == "Yes"


def test_is_rotated_two_places_example_2():
    """
    Example 2:
    Input: str1 = “amazon”, str2 = “onamaz”
    Output: Yes
    Explanation: Rotating string1 by 2 places in clockwise gives the string2.
    """
    str1 = "amazon"
    str2 = "onamaz"
    assert is_rotated_two_places(str1, str2) == "Yes"


# Custom tests
def test_is_rotated_two_places_example_3():
    """
    Example 3:
    Input: str1 = "nathan", str2 = "nlutala"
    Output: No
    """
    str1 = "nathan"
    str2 = "nlutala"
    assert is_rotated_two_places(str1, str2) == "No"


def test_is_rotated_two_places_example_4():
    """
    Example 4:
    Input: str1 = "rain", str2 = "inar"
    Output: No
    Explanation: Rotating string1 by 2 places in clockwise gives the string2.
    """
    str1 = "rain"
    str2 = "inar"
    assert is_rotated_two_places(str1, str2) == "No"
