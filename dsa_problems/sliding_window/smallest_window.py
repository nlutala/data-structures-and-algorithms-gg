"""
A file to tackle the example coding interview question as found on the website below:
https://www.geeksforgeeks.org/find-the-smallest-window-in-a-string-containing-all-characters-of-another-string/

Author: Nathan Lutala (nlutala)
"""


def find_smallest_window(s: str, p: str) -> str:
    """
    Given two strings S (length m) and P (length n), the task is to find the smallest
    substring in S that contains all characters of P, including duplicates. If no such
    substring exists, return "-1". If multiple substrings of the same length are found,
    return the one with the smallest starting index.\n

    :param - s (a string)\n
    :param - p (a string)\n

    Return the smallest substring in S that contains all characters of P, including
    duplicates.
    """
    if len(s) < len(p):
        return "-1"
    elif len(s) == len(p):
        return s if sorted(s) == sorted(p) else "-1"
    else:
        window_len = len(p)

        while window_len <= len(s):
            for i in range(len(s) - window_len + 1):
                window = s[i : i + window_len]
                validate_string = [
                    "1" for w in list(set(list(window))) if w in set(list(p))
                ]

                if "".join(validate_string).count("1") == len(p):
                    return window

                print(window)

            window_len += 1

        return "-1"
