"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/given-a-sequence-of-words-print-all-anagrams-together/

Author: Nathan Lutala (nlutala)
"""


def group_anagrams(arr: list[str]) -> list[str]:
    """
    Given an array of integers arr[], The task is to find the index of first
    repeating element in it i.e. the element that occurs more than once and
    whose index of the first occurrence is the smallest. \n

    :param - arr (list of integers)\n

    returns the first element that repeats in the array.
    """
    # This could be implemented a lot better
    grouped_words = []
    new_arr = arr
    previous_word = []
    indexes = []

    while len(new_arr) != 0:
        for i, word in enumerate(new_arr):
            if not previous_word:
                previous_word = sorted(list(word))
                grouped_words.append(word)
                indexes.append(i)
            else:
                if previous_word == sorted(list(word)):
                    grouped_words.append(word)
                    indexes.append(i)

        previous_word = []
        new_arr = [new_arr[i] for i in range(len(new_arr)) if i not in indexes]

    return grouped_words
