"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/minimum-insertions-to-form-a-palindrome-with-permutations-allowed/

Author: Nathan Lutala (nlutala)
"""


def min_insertions(string: str) -> int:
    """
    Given a string of lowercase letters. Find minimum characters to be
    inserted in the string so that it can become palindrome. We can change the
    positions of characters in the string.\n

    :param - string (a string)\n

    returns the minimum number of insertions to make the string a palindrome.
    """
    string_letters = list(set(list(string)))

    if string_letters == reversed(string_letters):
        return 0
    else:
        freq = {}

        for s in string_letters:
            freq[s] = string.count(s)

        new_word = ""

        for f in freq:
            if freq.get(f) % 2 == 0:
                new_word = (f * (freq.get(f) // 2)) + new_word + (f * (freq.get(f) // 2))
            else:
                new_word = (
                    new_word[0 : len(new_word) // 2]
                    + (f * freq.get(f))
                    + new_word[(len(new_word) // 2) :]
                )

        if list(new_word) == reversed(list(new_word)):
            return 0
        else:
            print(new_word)
            result = 0

            for i in range(len(new_word)):
                if new_word[i] != new_word[len(new_word)-1-i]:
                    result += 1

            return result
