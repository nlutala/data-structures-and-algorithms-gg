"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/find-the-minimum-distance-between-the-given-two-words/

Author: Nathan Lutala (nlutala)
"""


def min_distance(s: list[str], word1: str, word2: str) -> int:
    """
    Given a list of words followed by two words, the task is to find the
    minimum distance between the given two words in the list of words.\n

    :param - s (list of strings)\n
    :param - word1 (a string)\n
    :param - word2 (a string)\n

    returns the minimum distance between two words in a list of words.
    """
    min_distance = -1
    word1_index = None
    word2_index = None

    for i, word in enumerate(s):
        if word == word1:
            word1_index = i

        if word == word2:
            word2_index = i

        if word1_index is not None and word2_index is not None:
            if min_distance == -1 or min_distance > word2_index - word1_index:
                min_distance = word2_index - word1_index

    return min_distance
