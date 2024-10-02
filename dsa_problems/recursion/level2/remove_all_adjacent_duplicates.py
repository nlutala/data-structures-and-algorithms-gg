"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/recursively-remove-adjacent-duplicates-given-string/

Author: Nathan Lutala (nlutala)
"""


def remove_duplicates(s: str) -> str:
    """
    Given a string S, the task is to remove all its adjacent duplicate
    characters recursively.\n

    :param - s (a a string)\n

    returns a new string with adjacent duplicate characters removed.
    """

    first_repeating_char = ""

    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            first_repeating_char = s[i]
            break

    if first_repeating_char != "":
        s = [letter for letter in s if letter != first_repeating_char]
        return remove_duplicates("".join(s))

    return s
