"""
A file to tackle the example coding interview question as found on the website below:
https://www.geeksforgeeks.org/smallest-window-contains-characters-string/

Author: Nathan Lutala (nlutala)
"""


def window_with_all_chars(string: str) -> str:
    """
    Given a string, find the smallest window length with all distinct
    characters of the given string. For eg. str = “aabcbcdbca”, then the
    result would be 4 as of the smallest window will be “dbca” .\n

    :param - string (a string)\n

    Returns the smallest substring containing all the characters of the whole
    string.
    """
    all_chars = sorted(list(set(list(string))))
    window_len = len(all_chars)

    while window_len <= len(string):
        for i in range(len(string) - window_len + 1):
            window = string[i : i + window_len]

            if sorted(list(set(list(window)))) == all_chars:
                return window

        window_len += 1

    return f"No shortest string found containing letters {', '.join(all_chars)}"
