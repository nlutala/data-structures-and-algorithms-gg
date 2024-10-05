"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/find-equal-point-string-brackets/

Author: Nathan Lutala (nlutala)
"""


def equal_point(string: str) -> int:
    """
    Given a string of brackets, the task is to find an index k which decides
    the number of opening brackets is equal to the number of closing brackets.
    The string must be consists of only opening and closing brackets i.e.
    ‘(‘ and ‘)’.\n

    :param - string (a string of opening '(' and closing ')' parantheses)\n

    Returns the equal point (an index such that the number of opening brackets
    before it is equal to the number of closing brackets from and after).
    """

    for i in range(len(string)):
        first_section = string[0 : i + 1]
        second_section = string[i + 1 :]

        if first_section.count("(") == second_section.count(")"):
            return i + 1
