"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/frequency-of-each-character-in-a-string-using-unordered_map-in-c/

Author: Nathan Lutala (nlutala)
"""


def char_frequency(string: str) -> list[list]:
    """
    Given a string str, the task is to find the frequency of each character of
    a string.\n

    :param - string (a string hehe)\n

    returns a list of lists (character, frequency).
    """
    frequencies = {}

    for s in string:
        if frequencies.get(s, 0) == 0:
            frequencies[s] = 1
        else:
            frequencies[s] = frequencies.get(s) + 1

    return [[f, frequencies.get(f)] for f in frequencies]


if __name__ == "__main__":

    def test_char_frequency_example_1():
        """
        Example 1:
        Input: str = "geeksforgeeks"
        Output:
        r 1
        e 4
        s 2
        g 2
        k 2
        f 1
        o 1
        """
        string = "geeksforgeeks"

        return char_frequency(string) == [
            ["g", 2],
            ["e", 4],
            ["k", 2],
            ["s", 2],
            ["f", 1],
            ["o", 1],
            ["r", 1],
        ]

    def test_char_frequency_example_2():
        """
        Example 2:
        Input: str = "programming"
        Output:
        n 1
        i 1
        p 1
        o 1
        r 2
        a 1
        g 2
        m 2
        """
        string = "programming"

        return char_frequency(string) == [
            ["p", 1],
            ["r", 2],
            ["o", 1],
            ["g", 2],
            ["a", 1],
            ["m", 2],
            ["i", 1],
            ["n", 1]
        ]

    print(
        test_char_frequency_example_1(),
        test_char_frequency_example_2(),
    )
