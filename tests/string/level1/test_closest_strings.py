"""
A file tests the min_distance function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.string.level1.closest_strings import min_distance


def test_min_distance_example_1():
    """
    Example 1:
    Input: S = ["the", "quick", "brown", "fox", "quick"], word1 = "the", word2 = "fox"
    Output: 3
    Explanation: Minimum distance between the words "the" and "fox" is 3
    """
    words = ["the", "quick", "brown", "fox", "quick"]
    word1, word2 = "the", "fox"
    assert min_distance(words, word1, word2) == 3


def test_min_distance_example_2():
    """
    Example 2:
    Input: S = ["geeks", "for", "geeks", "contribute",  "practice"], word1 = "geeks",
    word2 = "practice"
    Output: 2
    Explanation: Minimum distance between the words "geeks" and "practice" is 2
    """
    words = ["geeks", "for", "geeks", "contribute", "practice"]
    word1, word2 = "geeks", "practice"
    assert min_distance(words, word1, word2) == 2


# Custom test
def test_min_distance_example_3():
    """
    Example 3:
    Input: S = ["do", "you", "like", "like", "chips"], word1 = "you", word2 = "like"
    Output: 3
    """
    words = ["do", "you", "like", "like", "chips"]
    word1, word2 = "you", "like"
    assert min_distance(words, word1, word2) == 1
