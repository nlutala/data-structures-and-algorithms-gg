"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/top-50-problems-on-hash-data-structure-asked-in-sde-interviews/

Author: Nathan Lutala (nlutala)
"""


def range_of_equal_1s_and_0s(arr: list[int]) -> str:
    """
    Given an array containing only 0s and 1s, find the largest subarray which contains
    equal no of 0s and 1s. The expected time complexity is O(n).\n

    :param - arr (list of integers)\n

    returns the range of numbers of equal 1s and 0s or 'No such subarray'.
    """

    if 1 in arr and 0 in arr:
        zero_count = [num for num in arr if num == 0]
        one_count = [num for num in arr if num == 1]

        if len(zero_count) == len(one_count):
            return f"0 to {len(arr)-1}"
        elif len(zero_count) < len(one_count):
            window_length = len(zero_count) * 2
        else:
            window_length = len(one_count) * 2

        length = 0
        starting = 0
        ending = 0

        for i in range(len(arr) - window_length + 1):
            start = i
            end = i + window_length
            subarray = arr[start:end]

            while len(subarray) > length:
                zero_count = [num for num in subarray if num == 0]
                one_count = [num for num in subarray if num == 1]

                if len(zero_count) == len(one_count):
                    length = len(subarray)
                    starting = start
                    ending = end - 1
                else:
                    end -= 1
                    subarray = arr[start:end]

        return f"{starting} to {ending}"

    return "No such subarray"
