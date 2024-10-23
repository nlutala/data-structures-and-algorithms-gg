"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/delete-consecutive-words-sequence/

Author: Nathan Lutala (nlutala)
"""


def remove_same_words(sentence: str) -> int:
    """
    Given a sequence of n strings, the task is to check if any two similar
    words come together and then destroy each other then print the number of
    words left in the sequence after this pairwise destruction.\n

    :param - sentence (a string)\n

    Returns how many words are in the sentence.
    """
    # Make the sentence a list (easier to work with)
    sentence_list = sentence.split(" ")

    stack = []

    for word in sentence_list:
        if len(stack) == 0:
            stack.insert(0, word)
        else:
            if stack[0] == word:
                stack.pop(0)
            else:
                stack.insert(0, word)

    return len(stack)
