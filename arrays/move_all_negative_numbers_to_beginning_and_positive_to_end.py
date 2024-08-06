"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/move-negative-numbers-beginning-positive-end-constant-extra-space/

Author: Nathan Lutala (nlutala)
"""


def move_negative_and_positive(array: list) -> list[int]:
    """
    An array contains both positive and negative numbers in random order.
    Rearrange the array elements so that all negative numbers appear before
    all positive numbers.

    :param - array (list)\n

    returns a list with negative numbers at the start and positive numbers to
    the end of the array.
    """
    # Again, this one is basically a sort, but the order of elements is not
    # important
    zero_index = 0
    result = [0]

    for num in array:
        if num >= 0:
            result.append(num)
        else:
            result.insert(zero_index, num)
        zero_index += 1
    
    result.pop(zero_index)

    return result
