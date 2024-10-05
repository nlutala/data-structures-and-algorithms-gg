"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/encrypt-the-string-2/

Author: Nathan Lutala (nlutala)
"""


def encrypt_string(s: str) -> str:
    """
    Given a string S consisting of N, lower case English alphabet, it is also
    given that a string is encrypted by first replacing every substring of the
    string consisting of the same character with the concatenation of that
    character and the hexadecimal representation of the size of the substring
    and then revering the whole string, the task is to find the encrypted
    string. \n

    :param - s (a string)\n

    returns the encrypted string.
    """
    encrypted_string = ""

    hex_and_chars = {"10": "a", "11": "b", "12": "c", "13": "d", "14": "e", "15": "f"}

    set_of_chars_in_string = []

    for char in s:
        if char not in set_of_chars_in_string:
            set_of_chars_in_string.append(char)

    for char in set_of_chars_in_string:
        if hex_and_chars.get(str(s.count(char))) is not None:
            encrypted_string += char + hex_and_chars.get(str(s.count(char)))
        else:
            encrypted_string += char + str(s.count(char))

    reverse_encrypted_string = [
        encrypted_string[i] for i in range(len(encrypted_string) - 1, -1, -1)
    ]

    encrypted_string = "".join(reverse_encrypted_string)

    return encrypted_string
