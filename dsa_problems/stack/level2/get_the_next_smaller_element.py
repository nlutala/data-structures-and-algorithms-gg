"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/find-the-nearest-smaller-numbers-on-left-side-in-an-array/

Author: Nathan Lutala (nlutala)
"""


def next_smaller_element(arr: list[int]) -> int:
    """
    Given an array of integers, find the nearest smaller number for every element such
    that the smaller element is on the left side.\n

    :param - arr (a list of integers)\n

    Return the next smaller element in the array.
    """
    comparison_number = arr[0]
    stack = []

    for num in arr[1:]:
        stack.append(num)

        if stack[-1] < comparison_number:
            return stack.pop()

    # return None - does not need to be explicit
