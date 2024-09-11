"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/roman-number-to-integer/https://www.geeksforgeeks.org/converting-decimal-number-lying-between-1-to-3999-to-roman-numerals/
Author: Nathan Lutala (nlutala)
"""


def int_to_roman_numeral(s: str) -> int:
    """
    Given a number, find its corresponding Roman numeral. \n

    :param - s (integer)\n

    returns the roman numeral form of an integer.
    """
    pass


if __name__ == "__main__":

    def test_int_to_roman_numeral_example_1():
        """
        Example 1:
        Input: 9
        Output: IX
        Explanation: IX is a Roman symbol which represents 9
        """
        s = 9
        return int_to_roman_numeral(s) == "IX"

    def test_int_to_roman_numeral_example_2():
        """
        Example 2:
        Input: 40
        Output: XL
        Explanation: XL is a Roman symbol which represents 40
        """
        s = 40
        return int_to_roman_numeral(s) == "XL"

    def test_int_to_roman_numeral_example_3():
        """
        Example 3:
        Input: MCMIV
        Output: 1904
        Explanation: MCMIV is a Roman symbol which represents 1094
        """
        s = 1904
        return int_to_roman_numeral(s) == "MCMIV"

    print(
        "Result for test_int_to_roman_numeral_example_1()".strip(),
        test_int_to_roman_numeral_example_1(),
        "\n",
        "Result for test_int_to_roman_numeral_example_2()".strip(),
        test_int_to_roman_numeral_example_2(),
        "\n",
        "Result for test_int_to_roman_numeral_example_3()".strip(),
        test_int_to_roman_numeral_example_3(),
    )
