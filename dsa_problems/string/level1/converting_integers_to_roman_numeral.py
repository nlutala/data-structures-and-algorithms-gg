"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/converting-decimal-number-lying-between-1-to-3999-to-roman-numerals/
Author: Nathan Lutala (nlutala)
"""


def int_to_roman_numeral(s: int) -> str:
    """
    Given a number, find its corresponding Roman numeral. \n

    :param - s (integer)\n

    returns the roman numeral form of an integer.
    """
    decimal_to_numeral = {
        "1": "I",
        "4": "IV",
        "5": "V",
        "9": "IX",
        "10": "X",
        "40": "XL",
        "50": "L",
        "90": "XC",
        "100": "C",
        "400": "CD",
        "500": "D",
        "900": "CM",
        "1000": "M",
    }

    numeral = ""
    total = s

    while total != 0:
        print(numeral, total)
        if decimal_to_numeral.get(str(total)) is not None:
            numeral += decimal_to_numeral.get(str(total))
            total -= total
        else:
            length_total = len(str(total))
            temp_number = 10 ** (length_total - 1) * int(str(total)[0])

            if decimal_to_numeral.get(str(temp_number)) is not None:
                numeral += decimal_to_numeral.get(str(temp_number))
            elif temp_number < 10 ** (length_total - 1) * 4:
                numeral += decimal_to_numeral.get(
                    str(10 ** (length_total - 1))
                ) * int(str(total)[0])
            elif temp_number > 10 ** (length_total - 1) * 5:
                numeral += decimal_to_numeral.get(
                    str(10 ** (length_total - 1) * 5)
                ) * (int(str(total)[0]) - 5)

            total -= temp_number

    return numeral
