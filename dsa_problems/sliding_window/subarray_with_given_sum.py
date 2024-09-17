"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/find-subarray-with-given-sum/

Author: Nathan Lutala (nlutala)
"""


def find_subarray_with_given_sum(arr: list[int], sum: int) -> list[int] | int:
    """
    Given a 1-based indexing array arr[] of integers and an integer sum, return the left
    and right indexes(1-based indexing) of that subarray. In case of multiple subarrays,
    return the subarray indexes which come first on moving from left to right. If no
    such subarray exists return an array consisting of element -1.\n

    :param - arr (list of integers)\n
    :param - sum (integer that the numbers in the subarray should add up to)\n

    return the subarray indexes which come first on moving from left to right. If no
    such subarray exists return an array consisting of element -1.
    """
    start = 0
    current_sum = None

    for i in range(len(arr)):
        if current_sum is not None:
            if current_sum == sum:
                return [start + 1, i]

            if current_sum + arr[i] <= sum:
                current_sum += arr[i]
            else:
                current_sum = current_sum - arr[start] + arr[i]
                start += 1
        else:
            current_sum = arr[start]

    return -1
