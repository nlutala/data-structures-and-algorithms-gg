"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/count-distinct-subsequences/

Author: Nathan Lutala (nlutala)
"""


def count_subsequences(string: str) -> int:
    """
    Given a string, find the count of distinct subsequences of it.\n

    :param - string (a string)\n

    returns the number of distinct subsequences of all letters in the string.
    """
    subsequences = set("")
    window = 1

    for i in range(len(string)):
        for i in range(len(string) - window + 1):
            subsequences.add(string[i : window + 1])

        window += 1

    # Now add subsequences where some characters are missing
    letters = set(list(string))
    extra_count = 0

    for letter in letters:
        new_string = string.replace(letter, "")

        if len(new_string) > 1:
            extra_count += len(new_string)

    return len(list(subsequences)) + extra_count
