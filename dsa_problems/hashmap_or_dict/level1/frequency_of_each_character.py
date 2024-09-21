"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/frequency-of-each-character-in-a-string-using-unordered_map-in-c/

Author: Nathan Lutala (nlutala)
"""


def char_frequency(string: str) -> list[list]:
    """
    Given a string str, the task is to find the frequency of each character of
    a string.\n

    :param - string (a string hehe)\n

    returns a list of lists (character, frequency).
    """
    freq = {}

    for s in string:
        if freq.get(s) is None:
            freq[s] = string.count(s)

    return [[s, freq.get(s)] for s in freq]
