"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/next-greater-element/

Author: Nathan Lutala (nlutala)
"""


def next_greater_element(arr: list[int]) -> int:
    """
    Given an array, print the Next Greater Element (NGE) for every element.\n

    Note: The Next greater Element for an element x is the first greater element on the
    right side of x in the array. Elements for which no greater element exist, consider
    the next greater element as -1.\n

    :param - arr (a list of integers)\n

    Return the next greater element in the array.
    """

    stack = []
    element = arr[0]

    for a in arr:
        if len(stack) == 0:
            stack.insert(0, a)
        else:
            if stack[0] > element:
                return stack[0]
            else:
                stack = stack[1:]
                stack.insert(0, a)

    return -1
