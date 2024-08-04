"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/c-program-to-sort-an-array-in-ascending-order/

Author: Nathan Lutala (nlutala)
"""


def sort_array_asc(array: list) -> list:
    """
    Sorting an array in ascending order means arranging the elements from
    smallest element to largest element.

    :param - array (list)

    returns the sorted array
    """
    array_tracker = array
    new_array = []

    while len(new_array) != len(array):
        try:
            smallest = array_tracker[0]

            for i in range(len(array_tracker)):
                if smallest > array_tracker[i]:
                    smallest = array_tracker[i]

            new_array.append(smallest)
            array_tracker.remove(smallest)
        except IndexError:
            pass

    return new_array
