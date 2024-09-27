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

    while current_index < len(arr):
        elem = arr[current_index]
        window = arr[current_index : current_index + elem]

        if elem > len(window):
            current_index += elem
        else:
            max_index = [i for i, w in enumerate(window) if w == max(window)]
            current_index += max_index[-1] + 1

        num_of_jumps += 1
        # print(current_index)

    if len(list(set(arr))) == 1:
        num_of_jumps -= 1

    return num_of_jumps
