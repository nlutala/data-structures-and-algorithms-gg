"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/print-1-to-n-without-using-loops/

Author: Nathan Lutala (nlutala)
"""


def print_1_to_n(n: int) -> None:
    """
    You are given an integer N. Print numbers from 1 to N without the help of
    loops.\n

    :param - n (the number to print to)\n
    """
    # if n > 0:
    #     print(n)
    #     return print_1_to_n(n - 1)

    if n > 0:
        print_1_to_n(n - 1)
        print(n, end="  ")


if __name__ == "__main__":
    print_1_to_n(5)
