"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/find-the-minimum-distance-between-the-given-two-words/

Author: Nathan Lutala (nlutala)
"""


def min_distance(words: list[str], word1: str, word2: str) -> int:
    """
    Given a list of words followed by two words, the task is to find the minimum
    distance between the given two words in the list of words.\n

    :param - words (a list of strings)\n
    :param - str1 (a string)\n
    :param - str2 (a string)\n

    returns the minimum distance between two words.
    """
    word1_occurrences = [i for i in range(len(words)) if words[i] == word1]
    word2_occurrences = [i for i in range(len(words)) if words[i] == word2]

    # Not optimal but I used a set for storing just incase there are duplicate distances
    distances = set()

    for w1 in word1_occurrences:
        for w2 in word2_occurrences:
            distances.add(abs(w1 - w2))

    return min(list(distances))
