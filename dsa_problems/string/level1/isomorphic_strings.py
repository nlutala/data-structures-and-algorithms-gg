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
    str1_set = list(set(str1))
    str2_set = list(set(str2))

    if len(str1_set) == len(str2_set):
        str1_dict = {}

        for char in str1_set:
            if char not in str1_dict.keys():
                str1_dict[char] = str1.count(char)

        str2_dict = {}

        for char in str2_set:
            if char not in str2_dict.keys():
                str2_dict[char] = str2.count(char)

        str1_count_list = sorted(list(str1_dict.values()))
        str2_count_list = sorted(list(str2_dict.values()))

        if str1_count_list == str2_count_list:
            return True

    return False
