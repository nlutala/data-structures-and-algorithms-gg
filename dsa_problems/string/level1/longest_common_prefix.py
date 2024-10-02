"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/longest-common-prefix-using-sorting/

Author: Nathan Lutala (nlutala)
"""


def longest_prefix(strs: list[str]) -> str | int:
    """
    Given an array of strings strs[]. The task is to return the longest common
    prefix among each and every strings present in the array. If there's no
    prefix common in all the strings, return "-1".\n

    :param - strs (list of strings)\n

    returns the longest common prefix or -1 if there's no common prefix in the
    given strings.
    """
    # 1. Get the longest word
    longest_word_length = 0

    for s in strs:
        if len(s) > longest_word_length:
            longest_word_length = len(s)

    longest_word = [word for word in strs if len(word) == longest_word_length][0]

    # 2. Remove the longest word from the rest
    remaining_strs = [s for s in strs if s != longest_word]

    # 3. Loop through the rest comparing the letters (if that makes sense)
    longest_prefix = ""

    for i in range(len(longest_word)):
        prefix = longest_word[i:i+1]
        count = 0
        for rs in remaining_strs:
            if prefix == rs[i:i+1]:
                count += 1

        if count == len(remaining_strs):
            longest_prefix += prefix
        else:
            return longest_prefix if len(longest_prefix) > 0 else -1

    return longest_prefix
