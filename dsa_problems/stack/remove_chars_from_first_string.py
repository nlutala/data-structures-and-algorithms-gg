"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/remove-characters-from-the-first-string-which-are-present-in-the-second-string/

Author: Nathan Lutala (nlutala)
"""


def remove_chars(string1: str, string2: str) -> str:
    """
    Given two strings string1 and string2, remove those characters from the
    first string(string1) which are present in the second string(string2).
    Both strings are different and contain only lowercase characters.\n

    NOTE: The size of the first string is always greater than the size of the
    second string( |string1| > |string2|).\n

    :param - string1 (a string)\n
    :param - string2 (a string)\n

    Return a new string derived from string 1 removing the letters in string 2.
    """
    result = ""
    letters_to_remove = list(string2)

    for letter in string1:
        if letter in letters_to_remove:
            letters_to_remove.remove(letter)
        else:
            result += letter

    return result
