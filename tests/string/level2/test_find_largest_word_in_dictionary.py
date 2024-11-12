"""
A file tests the get_largest_word function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.string.level2.find_largest_word_in_dictionary import get_largest_word


def test_get_largest_word_example_1():
    """
    Example 1:
    Input : dict = {"ale", "apple", "monkey", "plea"}, str = "abpcplea"
    Output : apple
    """
    dictionary, string = ["ale", "apple", "monkey", "plea"], "abpcplea"
    assert get_largest_word(dictionary, string) == "apple"


def test_get_largest_word_example_2():
    """
    Example 2:
    Input  : dict = {"pintu", "geeksfor", "geeksgeeks", "forgeek"},
    str = "geeksforgeeks"
    Output : geeksgeeks
    """
    dictionary = ["pintu", "geeksfor", "geeksgeeks", "forgeek"]
    string = "geeksforgeeks"
    assert get_largest_word(dictionary, string) == "geeksgeeks"


# Custom tests - Still not convinced this works well...
def test_get_largest_word_example_3():
    """
    Example 3:
    Input  : dict = {"atoi", "pintu", "literally", "geeks", "forgeek"},
    str = "literallygeeks"
    Output : literally
    """
    dictionary = ["atoi", "pintu", "literally", "geeks", "forgeek"]
    string = "literallygeeks"
    assert get_largest_word(dictionary, string) == "literally"


def test_get_largest_word_example_4():
    """
    Example 4:
    Input  : dict = {"atoi", "pintu", "literal", "geeks", "forgeek"},
    str = "atoialiterallygeeks"
    Output : literal
    """
    dictionary = ["atoi", "pintu", "literal", "geeks", "forgeek"]
    string = "atoialiterallygeeks"
    assert get_largest_word(dictionary, string) == "literal"


def test_get_largest_word_example_5():
    """
    Example 5:
    Input  : dict = {"atoi", "pintu", "literal", "geeks", "forgeek"},
    str = "atoialiterallygeeks"
    Output : literal
    """
    dictionary = ["atoi", "pintu", "literal", "geeks", "forgeek"]
    string = "latelralretoil"
    assert get_largest_word(dictionary, string) == "atoi"
