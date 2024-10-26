"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/write-your-own-atoi/

Author: Nathan Lutala (nlutala)
"""


def atoi(s: str) -> int:
    """
    Given a string s, the objective is to convert it into integer format
    without utilizing any built-in functions. Refer the below steps to know
    about atoi() function.\n

    :param - s (a string denoting a number)\n

    Cases for atoi() conversion:
    - Skip any leading whitespaces.\n
    - Check for a sign (‘+’ or ‘-‘), default to positive if no sign is
      present.\n
    - Read the integer by ignoring leading zeros until a non-digit character
      is encountered or end of the string is reached. If no digits are
      present, print 0.\n
    - If the integer is greater than 231 – 1, then print 231 – 1 and if the
      integer is smaller than -231, then print -231.

    return the integer representation of the string.
    """
    numbers = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
    }

    temp_s = ""

    for i in range(len(s)):
        if s[i] in numbers:
            temp_s += s[i]
        elif temp_s == "" and s[i] in {"+", "-"}:
            temp_s += s[i]
        elif s[i] == " ":
            continue
        else:
            break

    print(temp_s)

    is_positive = True

    result = 0

    for i in range(len(temp_s)):
        print(result)
        if i == 0 and temp_s[i] == "-":
            is_positive = False
        else:
            multiple_of_ten = len(temp_s) - 1 - i
            result += numbers.get(temp_s[i], 0) * (10**multiple_of_ten)

    if is_positive:
        if result > (2**31) - 1:
            return (2**31) - 1

        return result
    else:
        result *= -1
        if result < (2**31) * -1:
            return (2**31) * -1

        return result
