"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/sort-stack-using-temporary-stack/

Author: Nathan Lutala (nlutala)
"""


def sort_stack(arr: list[int]) -> int:
    """
    Given a stack of integers, sort it in ascending order using another
    temporary stack.\n

    :param - arr (a list of integers represented by a stack)\n

    Return a sorted stack in asceding order.
    """
    if len(arr) < 2:
        return arr

    maximum = None
    temp_arr = arr
    sorted_arr = []

    while temp_arr != []:
        for num in temp_arr:
            if maximum is None:
                maximum = num
            elif maximum < num:
                maximum = num

        sorted_arr.insert(0, maximum)

        # Remove maximum from temp_arr (in a stack fashion)
        max_index = temp_arr.index(maximum)
        temp_arr = temp_arr[0:max_index] + temp_arr[max_index + 1 :]
        temp_arr = temp_arr[::-1]

        # Set maximum back to None
        maximum = None

    return sorted_arr
