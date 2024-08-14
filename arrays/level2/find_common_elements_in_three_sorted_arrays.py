"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/find-common-elements-three-sorted-arrays/

Author: Nathan Lutala (nlutala)
"""


def find_common_elements(a: list, b: list, c: list) -> list:
    """
    Given three sorted arrays in non-decreasing order, print all common
    elements in these arrays.\n

    Note: In case of duplicate common elements, print only once.\n

    :param - a (list)\n
    :param - b (list)\n
    :param - c (list)\n

    returns a list of the elements that are common in the three arrays.
    """
    all_elements = sorted(list(set(a + b + c)))
    common_elements = [
        elem for elem in all_elements if elem in a and elem in b and elem in c
    ]

    return common_elements if common_elements else None
