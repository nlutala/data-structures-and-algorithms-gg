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

    while True:
        try:
            smallest = array_tracker[0]
            for i, value in enumerate(array_tracker):
                if value < smallest:
                    smallest = value

            array_tracker.remove(smallest)
            new_array.append(smallest)
        except IndexError:
            return new_array
