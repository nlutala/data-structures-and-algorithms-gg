"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/height-complete-binary-tree-heap-n-nodes/

Author: Nathan Lutala (nlutala)
"""

from math import log2


def height_of_tree(n: int) -> int:
    """
    Consider a Binary Heap of size N. We need to find the height of it.\n

    :param - n (an integer denoting the number of nodes)\n

    Returns the height of the tree.
    """
    # Think about it this way:
    # The number of nodes in a complete tree is 2**h - 1, where h is the height of
    # the tree.
    # To find h, you will need to find the the log2 of n + 1 for the height h
    return int(log2(n + 1))
