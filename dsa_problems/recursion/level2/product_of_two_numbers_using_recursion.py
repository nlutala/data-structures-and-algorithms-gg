"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/product-2-numbers-using-recursion/

Author: Nathan Lutala (nlutala)
"""


def product(x: int, y: int) -> int:
    """
    Given two numbers x and y find the product using recursion.\n

    :param - x (an integer)\n
    :param - y (an integer)\n

    returns the product of two numbers.
    """

    if 0 in [x, y]:
        return 0
    else:
        # This is for when x and y are both positive
        if x < 0 and y < 0:
            return product(abs(x), abs(y))
        # The following 2 elifs are for the case in which x or y (not both) are negative
        elif x < 0 and y > 0:
            return x + product(x, y - 1)
        elif x > 0 and y < 0:
            return y + product(x - 1, y)
        else:
            if x >= y:
                return x + product(x, y - 1)
            else:
                return y + product(x - 1, y)
