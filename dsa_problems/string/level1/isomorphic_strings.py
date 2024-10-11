"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/check-if-two-given-strings-are-isomorphic-to-each-other/

Author: Nathan Lutala (nlutala)
"""


def is_isomorphic(str1: str, str2: str) -> bool:
    """
    Two strings str1 and str2 are called isomorphic if there is a one-to-one mapping
    possible for every character of str1 to every character of str2. And all occurrences
    of every character in ‘str1’ map to the same character in ‘str2’.\n

    :param - str1 (string)\n
    :param - str2 (string)\n

    returns True if all the occurrences of every character in str1 is the same as str2.
    False if otherwise
    """
    id = 0

    # For str1 first
    str1_dict = {}

    for char in str1:
        if str1_dict.get(char) is None:
            str1_dict[char] = id
            id += 1

    id = 0

    # For str2
    str2_dict = {}

    for char in str2:
        if str2_dict.get(char) is None:
            str2_dict[char] = id
            id += 1

    # If one string has more different letters than another, return False
    if len(str1_dict) != len(str2_dict):
        return False

    str1_representation = [str1_dict.get(char) for char in str1]
    str2_representation = [str2_dict.get(char) for char in str2]

    for i in range(len(str1)):
        if str1_representation[i] != str2_representation[i]:
            return False

    return True
