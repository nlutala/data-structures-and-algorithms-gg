"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/print-n-to-1-without-loop/

Author: Nathan Lutala (nlutala)
"""


def print_n_to_1(n: int) -> None:
    """
    You are given an integer N. Print numbers from N to 1 without the help of
    loops.\n

    :param - n (the number to print to)\n
    """
    if n > 0:
        print(n, end="  ")
        return print_n_to_1(n - 1)


if __name__ == "__main__":
    print_n_to_1(5)
    print("")
    print_n_to_1(10)
