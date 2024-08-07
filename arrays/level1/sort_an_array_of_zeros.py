"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/sort-an-array-of-0s-1s-and-2s/

Author: Nathan Lutala (nlutala)
"""


def sort_array_012(array: list) -> int:
    """
    Given an array A[] consisting of only 0s, 1s, and 2s. The task is to sort
    the array, i.e., put all 0s first, then all 1s and all 2s in last.

    :param - array (list)\n
    :param - x (int)\n

    returns the number of the number x in the array
    """
    # My thoughts is that this problem is the same as sorting something in 
    # ascending order

    new_array = []
    original_array = array.copy()

    while len(original_array) != 0:
        smallest = original_array[0]

        for value in original_array:
            smallest = value if value < smallest else smallest

        new_array.append(smallest)
        original_array.remove(smallest)

    return new_array
