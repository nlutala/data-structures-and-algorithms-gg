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
    temp_arr = arr
    remaining = sum

    # a + b + c = sum
    for i, elem in enumerate(arr):
        temp_arr = arr[0:i] + arr[i + 1 :]
        # sum - a = b + c
        if remaining >= elem:
            # remaining = sum - a
            remaining -= elem
            temp_arr = [a for a in temp_arr if a <= remaining]

            for j, b in enumerate(temp_arr):
                temp_arr_2 = temp_arr[0:j] + temp_arr[j + 1 :]
                # If remaining - b is in the array (return a, b and remaining - b)
                # remaining - b = c
                if remaining - b in temp_arr_2:
                    return sorted([elem, b, remaining - b])
