"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/check-string-can-obtained-rotating-another-string-2-places/

Author: Nathan Lutala (nlutala)
"""


def is_rotated_two_places(str1: str, str2: str) -> str:
    """
    Given two strings, str1 and str2, the task is to determine if str2 can be obtained
    by rotating str1 exactly 2 places in either a clockwise or anticlockwise
    direction.\n

    :param - str1 (a string)\n
    :param - str2 (a string)\n

    returns "Yes" if str2 is the rotated version of str1. "No" if otherwise.
    """
    clockwise_str1 = str1[2:] + str1[:2]
    anticlockwise_str1 = str1[len(str1) - 2 :] + str1[: len(str1) - 2]

    if clockwise_str1 == str2 or anticlockwise_str1 == str2:
        return "Yes"

    return "No"
