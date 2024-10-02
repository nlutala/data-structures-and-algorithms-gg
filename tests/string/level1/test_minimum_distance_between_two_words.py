"""
A file tests the min_distance function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.string.level1.minimum_distance_between_two_words import (
    min_distance,
)


def test_min_distance_example_1():
    """
    Example 1:
    Input: S = {"the", "quick", "brown", "fox", "quick"}, word1 = "the", word2 = "fox"
    Output: 3
    Explanation: Minimum distance between the words "the" and "fox" is 3
    """
    s = ["the", "quick", "brown", "fox", "quick"]
    word1 = "the"
    word2 = "fox"
    assert min_distance(s, word1, word2) == 3


def test_min_distance_example_2():
    """
    Example 2:
    Input: S = {"geeks", "for", "geeks", "contribute",  "practice"}, word1 = "geeks", word2 = "practice"
    Output: 2
    Explanation: Minimum distance between the words "geeks" and "practice" is 2
    """
    s = ["geeks", "for", "geeks", "contribute", "practice"]
    word1 = "geeks"
    word2 = "practice"
    assert min_distance(s, word1, word2) == 2
