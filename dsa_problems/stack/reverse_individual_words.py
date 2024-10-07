"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/reverse-individual-words/

Author: Nathan Lutala (nlutala)
"""


def reverse_string(string: str) -> str:
    """
    Given string str, we need to print the reverse of individual words.\n

    :param - string (a string)\n

    Return the reversed string.
    """
    # Split the string into a list of words
    words = string.split(" ")
    reversed_words = []

    for word in words:
        reversed_words.append(word[::-1])

    return " ".join(reversed_words)
