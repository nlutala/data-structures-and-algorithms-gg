"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/stack-set-3-reverse-string-using-stack/

Author: Nathan Lutala (nlutala)
"""


def reverse_string(string: str) -> str:
    """
    Given a string, reverse it using stack.\n

    :param - string (the string)\n

    Return the reversed string
    """
    reversed_word = ""

    for s in string:
        reversed_word = s + reversed_word

    return reversed_word


if __name__ == "__main__":

    def test_reverse_string_example_1():
        """
        Example 1:
        Input: str = “GeeksQuiz”
        Output: ziuQskeeG
        """
        string = "GeeksQuiz"
        return reverse_string(string) == "ziuQskeeG"


    def test_reverse_string_example_2():
        """
        Example 2:
        Input: str = “abc”
        Output: cba
        """
        string = "abc"
        return reverse_string(string) == "cba"

    print(
        test_reverse_string_example_1(),
        test_reverse_string_example_2(),
    )
