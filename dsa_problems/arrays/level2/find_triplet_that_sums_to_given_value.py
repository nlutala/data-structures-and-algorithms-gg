"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/

Author: Nathan Lutala (nlutala)
"""


def three_sum(arr: list[int], sum: int) -> list[int] | None:
    """
    Given an array arr[] of size n and an integer sum. Find if there’s a
    triplet in the array which sums up to the given integer sum.\n

    :param - arr (list of integers)\n
    :param - sum (integer)

    returns a list with the triple that add up to the sum.
    """
    remaining = sum

    for a in arr:
        numbers_less_than = [num for num in arr if num <= remaining - a and num != a]
        numbers_less_than = numbers_less_than[0 : len(numbers_less_than) - 1]

        if len(numbers_less_than) != 0:
            remaining -= a

            numbers_less_than = [num for num in arr if num <= remaining and num != a]

            for num in numbers_less_than:
                if remaining - num in numbers_less_than:
                    return sorted([a, num, remaining - num])
