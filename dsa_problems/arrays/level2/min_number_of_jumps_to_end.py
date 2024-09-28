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
    num_of_jumps = 0
    current_index = 0

    while current_index < len(arr) - 1:
        elem = arr[current_index]

        if elem > 1:
            elem += 1

        window = arr[current_index : current_index + elem]
        max_index = [i for i, w in enumerate(window) if w == max(window)]

        if len(list(set(window))) == 1:
            current_index += window[0]
        else:
            if max_index[-1] == 0:
                current_index += current_index + elem
            else:
                current_index += max_index[-1]

        num_of_jumps += 1

    return num_of_jumps
