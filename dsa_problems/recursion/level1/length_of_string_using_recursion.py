"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/program-for-length-of-a-string-using-recursion/

Author: Nathan Lutala (nlutala)
"""


def string_length(string: str) -> str:
    """
    Given a string calculate length of the string using recursion.\n

    :param - string (a string)\n

    Return the length of the string.
    """
    if len(string) == 1:
        return 1
    else:
        return 1 + string_length(string[1:])
