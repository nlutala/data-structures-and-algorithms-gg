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
        index = 0
        jumps = 0
        current_num = arr[index]

        while index < len(arr) - 1:
            sub_arr = arr[index:index+current_num+1]

            if sub_arr == []:
                return jumps

            num_dict = {}

            for i, num in enumerate(sub_arr):
                num_dict[str(num)] = i + 1

            index += num_dict.get(str(max(sub_arr)))
            jumps += 1
      
        return jumps
