"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/find-largest-word-dictionary-deleting-characters-given-string/

Author: Nathan Lutala (nlutala)
"""


def get_largest_word(dictionary: list[str], string: str) -> str:
    """
    Giving a dictionary and a string, find the longest string in dict which
    can be formed by deleting some characters of the given string.\n

    :param - dictionary (a list of strings)\n
    :param - string (a string)\n

    return the longest string in dict that can be formed after removing some
    letters.
    """
    # Sort the words in the dictionary by longest length to shortest length
    d = sorted(dictionary, key=len, reverse=True)

    # Loop through the words in the order (defined by d) to pick out the
    # longest word
    for word in d:
        word_in_string = "".join([letter for letter in string if letter in word])

        if word in word_in_string:
            return word
