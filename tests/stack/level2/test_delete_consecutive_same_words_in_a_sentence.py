"""
A file tests the remove_same_words function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.stack.level2.delete_consecutive_same_words_in_a_sequence import (
    remove_same_words,
)


def test_remove_same_words_example_1():
    """
    Example 1:
    Input : ab aa aa bcd ab
    Output : 3
    Explanation: As aa, aa destroys each other so, ab bcd ab is the new
    sequence.
    """
    sentence = "ab aa aa bcd ab"
    assert remove_same_words(sentence) == 3


def test_remove_same_words_example_2():
    """
    Example 2:
    Input :  tom jerry jerry tom
    Output : 0
    Explanation: As first both jerry will destroy each other. Then sequence
    will be tom, tom they will also destroy each other. So, the final sequence
    doesn’t contain any word.
    """
    sentence = "tom jerry jerry tom"
    assert remove_same_words(sentence) == 0
