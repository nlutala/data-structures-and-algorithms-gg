"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/kth-smallest-largest-element-in-unsorted-array/

Author: Nathan Lutala (nlutala)
"""


def find_kth_smallest_element(array: list, k: int) -> int:
    """
    Given an array arr[] of N distinct elements and a number K, where K is
    smaller than the size of the array. Find the K'th smallest element in the
    given array.

    :param - array (list)
    :param - k (int)

    returns the kth smallest integer
    """
    array_tracker = array
    new_array = []

    for i in range(k):
        smallest = array_tracker[0]
        for value in array_tracker:
            if value < smallest:
                smallest = value

        array_tracker.remove(smallest)
        new_array.append(smallest)
    
    return new_array[-1]
