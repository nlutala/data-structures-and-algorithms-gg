"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/rearrange-array-alternating-positive-negative-items-o1-extra-space/

Author: Nathan Lutala (nlutala)
"""


def rearrange_array_in_positive_and_negative(arr: list[int]) -> list[int]:
    """
    Given an array having positive and negative numbers, our task is to
    arrange them in an alternate fashion such that every positive number is
    followed by a negative number and vice-versa maintaining the order of
    appearance. The number of positive and negative numbers need not to be
    equal. If there are more positive numbers then they have to appear at the
    end of the array, same condition for negative numbers also.\n

    :param - arr (list of integers)\n

    returns a new list with alternating positive and negative integers.
    """
    negative_numbers = [num for num in arr if num < 0]
    positive_numbers = [num for num in arr if num >= 0]
    result = []

    while len(result) != len(arr):
        if len(negative_numbers) != 0:
            result.append(negative_numbers[0])
            negative_numbers = negative_numbers[1:]

        if len(positive_numbers) != 0:
            result.append(positive_numbers[0])
            positive_numbers = positive_numbers[1:]

    return result
