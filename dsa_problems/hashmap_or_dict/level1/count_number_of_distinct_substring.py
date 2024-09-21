"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/count-number-of-distinct-substring-in-a-string/

Author: Nathan Lutala (nlutala)
"""


def count_substring(string: str) -> int:
    """
    Given an array arr[] of length N, The task is to count all distinct
    elements in arr[].\n

    :param - arr (list of integers)\n

    returns a the number of distinct elements in the array.
    """
    # I'm treating this as a sliding wwindow question
    window_len = 1
    res = set()

    while window_len <= len(string):
        for i in range(len(string) - window_len + 1):
            window = string[i : i + window_len]

            if len(list(set(list(window)))) == len(window):
                res.add(window)

        window_len += 1

    return len(list(res))
