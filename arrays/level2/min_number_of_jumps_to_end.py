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
        index_covered = []

        while i < len(arr) - 1:
            index_covered.append(i)

            if index_covered[-1] >= len(arr):
                return jumps

            num = arr[i]
            sub_arr = arr[i:num+1]
            jumps += 1

            if sub_arr == []:
                return jumps

            if sub_arr[-1] < max(sub_arr):
                i += sub_arr.index(max(sub_arr)) + 1
            else:
                i += len(sub_arr)

        return jumps
