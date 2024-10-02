"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/roman-number-to-integer/

Author: Nathan Lutala (nlutala)
"""


def roman_number_to_int(s: str) -> int:
    """
    Given a string in roman form, the task is to convert this given roman
    string into an integer..\n

    :param - s (roman s)\n

    returns the integer form of a roman s.
    """
    value = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000,
    }

    r = 0
    value_added = 0

    for i in range(0, len(s)):
        try:
            if s[i] + s[i + 1] in ["IX", "IV", "XL", "XC", "CD", "CM"]:
                value_added = value.get(s[i + 1])
                r += value.get(s[i] + s[i + 1])
            else:
                r -= value_added
                r += value.get(s[i])
                value_added = 0
        except IndexError:
            r -= value_added
            r += value.get(s[i])

    return r
