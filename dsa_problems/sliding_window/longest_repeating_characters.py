"""
A file to tackle the example coding interview question as found on the website below:
https://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters/

Author: Nathan Lutala (nlutala)
"""


def longest_repeat(s: str) -> int | str:
    """
    Given a string s, find the length of the longest substring without repeating
    characters.\n

    :param - s (a string)\n

    Return the longest string from s with non-repeating characters.
    """
    if len(list(set(list(s)))) == len(s):
        return s
    else:
        window_len = len(s) - 1

        while window_len > 0:
            for i in range(len(s) - window_len):
                word = s[i : i + window_len]

                if len(word) == len(list(set(list(word)))):
                    return word

            window_len -= 1

        return ""
