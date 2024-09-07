"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/reverse-words-in-a-given-string/

Author: Nathan Lutala (nlutala)
"""


def reverse_string(string: str) -> str:
    """
    Given a string, the task is to reverse the order of the words in the given
    string.\n

    :param - string (str)\n

    returns the reversed string of the initial string.
    """
    # Split the string at an empty space to get the words
    words = string.split(" ")
    reversed_words = [words[i] for i in range(len(words) - 1, -1, -1)]

    return " ".join(reversed_words)


if __name__ == "__main__":

    def test_reverse_string_example_1():
        """
        Example 1:
        Input: s = "i love programming very much"
        Output: s = "much very programming love i"
        """
        s = "i love programming very much"

        return reverse_string(s) == "much very programming love i"

    def test_reverse_string_example_2():
        """
        Example 2:
        Input: s = "geeks for all"
        Output: s = "all for geeks"
        """
        s = "geeks for all"

        return reverse_string(s) == "all for geeks"

    print(test_reverse_string_example_1(), test_reverse_string_example_2())
