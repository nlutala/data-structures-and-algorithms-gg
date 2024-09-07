"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/find-subarray-with-given-sum/

Author: Nathan Lutala (nlutala)
"""


def find_subarray_with_sum(array: list, s: int) -> list[int]:
    """
    Given a 1-based indexing array arr[] of non-negative integers and an
    integer sum. You mainly need to return the left and right indexes(1-based
    indexing) of that subarray. In case of multiple subarrays, return the
    subarray indexes which come first on moving from left to right. If no such
    subarray exists return an array consisting of element -1.

    :param - array (list)\n
    :param - s (int) - the sum\n

    returns a list of the start and end of the subarray (or [-1] if the
    subarray) doesn't exist.
    """
    result = []
    current_sum = 0

    for i, value in enumerate(array):
        if current_sum == s and i != 0:
            return [result[0], result[-1]]
        elif value + current_sum < s:
            current_sum += value
            result.append(i)
        elif value + current_sum == s:
            result.append(i)
            return [result[0], result[-1]]
        else:
            if i != 0:
                current_sum -= array[result[0]]
                result = result[1:]

            result.append(i)
            current_sum += array[result[-1]]

    return [-1]
