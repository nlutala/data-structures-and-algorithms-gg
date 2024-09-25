"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/reverse-a-string-using-recursion/

Author: Nathan Lutala (nlutala)
"""


def reverse_string(string: str) -> str:
    """
    Write a recursive function to print the reverse of a given string.\n

    :param - string (a string)\n

    Return the reversed string of string.
    """
    if len(string) == 1:
        return string
    else:
        return string[-1] + reverse_string(string[:len(string)-1])
