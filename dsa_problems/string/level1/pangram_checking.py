"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/pangram-checking/

Author: Nathan Lutala (nlutala)
"""


# A pangram is a sentence containing every letter in the English Alphabet.
def is_pangram(string: str) -> str:
    """
    Given a string, the task is to check if it is Pangram or not.\n

    :param - string (a string)\n

    returns true of the string has all letters of the alphabet in it.
    """
    alphabet = list("abcdefghijklmnopqrstuvwxyz")

    for letter in alphabet:
        if letter not in string:
            return "is not a Pangram"

    return "is a Pangram"
