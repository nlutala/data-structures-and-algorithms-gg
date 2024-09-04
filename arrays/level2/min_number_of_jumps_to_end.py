"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/minimum-number-of-jumps-to-reach-end-of-a-given-array/

Author: Nathan Lutala (nlutala)
"""


def min_jumps(arr: list[int]) -> int:
    """
    Given an array arr[] where each element represents the max number of steps
    that can be made forward from that index. The task is to find the minimum
    number of jumps to reach the end of the array starting from index 0.\n

    :param - arr (list of heights as integers)\n

    minimum number of jumps needed to reach the end of the array.
    """
    arr_set = list(set(arr))

    if len(arr_set) == 1:
        return len(arr) - 1 // arr_set[0]
    else:
        i = 0
        jumps = 0

        while i < len(arr) - 1:
            num = arr[i]
            sub_arr = arr[i:i+num]

            sub_arr_set = list(set(sub_arr))

            if len(sub_arr_set) == 1:
                i += len(sub_arr)
            elif len(sub_arr_set) > 1:
                indexes_of_largest_number = [
                    i for i in range(len(sub_arr))
                    if sub_arr[i] == max(sub_arr)
                ]
                i += indexes_of_largest_number[-1] + 1
            else:
                return jumps

            print(i, jumps, sub_arr)
            jumps += 1

        return jumps
