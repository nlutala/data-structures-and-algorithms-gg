"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/license-key-formatting/

Author: Nathan Lutala (nlutala)
"""


def format_key(s: str, k: int) -> str:
    """
    Given a string S that consists of only alphanumeric characters and dashes.
    The string is separated into N + 1 groups by N dashes. Also given an
    integer K.\n

    We want to reformat the string S, such that each group contains exactly K
    characters, except for the first group, which could be shorter than K but
    still must contain at least one character. Furthermore, a dash must be
    inserted between two groups, and you should convert all lowercase letters
    to uppercase.\n

    :param - s (a string)\n
    :param - k (an integer)\n

    returns the formatted string.
    """
    # Step 1. Make everything capital letters
    s = s.upper()

    # Step 2. Remove all hyphens (add those in the end)
    s = s.replace("-", "")

    # Step 3. Group the strings so they have at least k characters
    first_group_size = k

    if len(s) % k != 0:
        first_group_size = len(s) % k

    formatted_key = s[:first_group_size]

    for i in range(first_group_size, len(s), k):
        formatted_key += f"-{s[i:i+k]}"

    return formatted_key
