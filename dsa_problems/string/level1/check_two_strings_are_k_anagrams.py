"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/top-50-string-coding-problems-for-interviews/

Author: Nathan Lutala (nlutala)
"""


def are_k_anagrams(str1: str, str2: str, k: int) -> str:
    """
    Given two strings of lowercase alphabets and a value k, the task is to find
    if two strings are K-anagrams of each other or not.\n

    Two strings are called k-anagrams if following two conditions are true:\n

    1. Both have same number of characters.\n
    2. Two strings can become anagram by changing at most k characters in a
       string.\n

    :param - str1 (a string)\n
    :param - str2 (a string)\n
    :param - k (an integer)\n

    returns "Yes" if str1 and str2 are k-anagrams of each other. "No" if
    otherwise.
    """
    # l (comes after k, meant to be a joke) 
    # but l is used to calculate the differences in the frequencies of letters
    # between str1 and str2. This should be less than or equal to k to return True
    # otherwise teh function returns False
    l = 0

    for r in list(set(list(str2))):
        l += abs(str1.count(r) - str2.count(r))

    return "Yes" if l <= k else "No"
