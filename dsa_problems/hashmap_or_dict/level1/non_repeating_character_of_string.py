"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/given-a-string-find-its-first-non-repeating-character/

Author: Nathan Lutala (nlutala)
"""


def first_non_repeating_char(string: str) -> int:
    """
    Given a string S of lowercase English letters, the task is to find the
    index of the first non-repeating character. If there is no such character,
    return -1.\n

    :param - string (a string hehe)\n

    returns the index of the first non-repating character (-1 if not found).
    """
    frequencies = {}

    for i, s in enumerate(list(string)):
        if frequencies.get(s) is None:
            frequencies[s] = [i]
        else:
            frequencies[s] = frequencies.get(s) + [i]

    for f in frequencies:
        if len(frequencies.get(f)) == 1:
            return frequencies.get(f)[0]

    return -1


if __name__ == "__main__":

    def test_first_non_repeating_char_example_1():
        """
        Example 1:
        Input: S = "geeksforgeeks"
        Output: 5
        Explanation: "f" is the first character in the string which does not
        repeat.
        """
        string = "geeksforgeeks"

        return first_non_repeating_char(string) == 5

    def test_first_non_repeating_char_example_2():
        """
        Example 2:
        Input: "aabbccc"
        Output: -1
        Explanation: All the characters in the given string are repeating
        """
        string = "aabbccc"

        return first_non_repeating_char(string) == -1

    print(
        test_first_non_repeating_char_example_1(),
        test_first_non_repeating_char_example_2(),
    )
