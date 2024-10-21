"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/reverse-a-stack-using-recursion/

Author: Nathan Lutala (nlutala)
"""


def reverse_stack(arr: list[int]) -> int:
    """
    Given a stack of integers, reverse it using recursion, without using
    loops.\n

    :param - arr (a list of integers represented by a stack)\n

    Return the reversed stack in asceding order.
    """
    if arr == []:
        return arr

    return reverse_stack(arr[1:]) + [arr[0]]
