"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/find-duplicates-in-on-time-and-constant-extra-space/

Author: Nathan Lutala (nlutala)
"""


def find_duplicates(array: list) -> list[int]:
    """
    Given an array of n elements that contains elements from 0 to n-1, with
    any of these numbers appearing any number of times. Find these repeating
    numbers in O(n) and use only constant memory space.\n

    Note: The repeating element should be printed only once.\n

    :param - arr (list)\n

    returns the repeating element.
    """
    result = []
    val_freq = {}

    for num in array:
        if val_freq.get(str(num)) is None:
            val_freq[str(num)] = 1
        else:
            val_freq[str(num)] = val_freq.get(str(num)) + 1
            result.append(num)

    return sorted(result)
