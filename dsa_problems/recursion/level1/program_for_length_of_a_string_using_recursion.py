"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/program-for-length-of-a-string-using-recursion/

Author: Nathan Lutala (nlutala)
"""


def length(string: str) -> int:
    """
    Given a string calculate length of the string using recursion.\n

    :param - string (a string)\n

    Return the length of the string.
    """
    if string == "":
        return 0

    return 1 + length(string[1:])
