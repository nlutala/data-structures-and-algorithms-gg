"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/kth-smallest-element-in-a-row-wise-and-column-wise-sorted-2d-array/

Author: Nathan Lutala (nlutala)
"""


def kth_smallest_element(k: int, array: list[list[int]]) -> int:
    """
    Given an n x n matrix, where every row and column is sorted in 
    non-decreasing order. Find the kth smallest element in the given 2D array.\n

    :param - k (an integer)\n
    :param - array (a 2D list of integers)\n

    The kth smallest element.
    """
    # Step 1. Flatten the list
    flattened_array = []

    for a in array:
        flattened_array += a

    # Step 2. Sort the array
    sorted_array = []
    smallest = None
    index = None

    for i in range(k):
        for j, elem in enumerate(flattened_array):
            if smallest is None:
                smallest = elem
                index = j
            else:
                if elem < smallest:
                    smallest = elem
                    index = j

        sorted_array.append(smallest)
        flattened_array = flattened_array[0:index] + flattened_array[index+1:]
        smallest = None

    # Step 3. Return the last element in the sorted array
    return sorted_array[-1]
