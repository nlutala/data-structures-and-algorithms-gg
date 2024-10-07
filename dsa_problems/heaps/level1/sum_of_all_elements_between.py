"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/top-50-problems-on-heap-data-structure-asked-in-interviews/

Author: Nathan Lutala (nlutala)
"""


def sum_of_elements(arr: list[int], k1: int, k2: int) -> int:
    """
    Given an array of integers and two numbers k1 and k2. Find the sum of all elements
    between given two k1’th and k2’th smallest elements of the array. It may be assumed
    that (1 <= k1 < k2 <= n) and all elements of array are distinct.\n

    :param - arr (a list of integers)\n
    :param - k1 (an integer denoting the number of nodes)\n
    :param - k2 (an integer denoting the number of nodes)\n

    Returns the sum of all the elements between k1 and k2.
    """
    # Sort the list
    arr.sort()

    # Return the sum of the numbers between k1 and k2
    return sum(arr[k1 : k2 - 1])
