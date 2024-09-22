"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/print-unique-words-string/

Author: Nathan Lutala (nlutala)
"""


def unique_words(string: str) -> list[str]:
    """
    Write a function that takes a String as an argument and prints all unique
    words in it.\n

    :param - string (a string)\n

    returns a list of all the unique words in the string.
    """
    # Remove any full stops or punctuation from the string
    new_string = ""

    for s in string:
        if s.isalpha():
            new_string += s
        else:
            new_string += " "

    unique_words = []

    for n in new_string.split(" "):
        if new_string.count(n) == 1:
            unique_words.append(n)

    for word in unique_words:
        print(word)

    return unique_words
