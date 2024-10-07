"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/minimum-product-k-integers-array-positive-integers/

Author: Nathan Lutala (nlutala)
"""


def min_product_no_heap(arr: list[int], k: int) -> int:
    """
    Given an array of n positive integers. We are required to write a program
    to print the minimum product of k integers of the given array.\n

    :param - arr (list of integers)\n
    :param - k (an integer)\n

    Retuns the product of the two smallest element in the given array.
    """
    # How I would implement this without using a heap
    sorted_arr = []
    smallest = arr[0]
    index = 0

    for i in range(k):
        for j in range(len(arr)):
            if smallest > arr[j]:
                smallest = arr[j]
                index = j

        sorted_arr.append(smallest)
        arr = arr[:index] + arr[index + 1 :]
        smallest = arr[0]

    product = 1

    for s in sorted_arr:
        product *= s

    return product


def min_product(arr: list[int], k: int) -> int:
    """
    Given an array of n positive integers. We are required to write a program
    to print the minimum product of k integers of the given array.\n

    :param - arr (list of integers)\n
    :param - k (an integer)\n

    Retuns the product of the two smallest element in the given array.
    """

    # How I would implement this using a heap (min heap)
    # It's a bit long, but I hope this makes sense
    class Node:
        def __init__(self, val: int, left: object, right: object):
            """
            Node constructor\n

            :param - val (integer of the node)\n
            :param - left (another node, with a value, left and right node,
            can be None)\n
            :param - right (another node, with a value, left and right node,
            can be None)\n
            """
            self.val = val
            self.left = left
            self.right = right

        def setLeft(self, node: object):
            """
            Update the left value of the node.\n

            :param - node (another node object)
            """
            self.left = node

        def setRight(self, node: object):
            """
            Update the right value of the node.\n

            :param - node (another node object)
            """
            self.left = node

        def addNode(self, node: object):
            """
            Add node based on it's value.\n

            :param - node (another node object)
            """
            if self.val > node.val:
                if self.left is None:
                    self.left = node
                else:
                    return self.left.addNode(node)
            elif self.val <= node.val:
                if self.right is None:
                    self.right = node
                else:
                    return self.right.addNode(node)

    root = Node(arr[0], None, None)

    for i in range(1, len(arr)):
        root.addNode(Node(arr[i], None, None))

    sorted_elems = []
    visited_nodes = []  # Stack - to keep track of parent nodes
    current_node = root

    for i in range(0, k):
        while current_node is not None:
            visited_nodes.append(current_node)
            current_node = current_node.left

        parent = visited_nodes.pop()
        sorted_elems.append(parent.val)
        current_node = parent.right

    product = 1

    for elem in sorted_elems:
        product *= elem

    return product
