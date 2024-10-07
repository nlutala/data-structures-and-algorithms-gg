"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/kth-smallest-largest-element-in-unsorted-array/

Author: Nathan Lutala (nlutala)
"""


def find_kth_smallest_no_heap(arr: list[int], k: int) -> int:
    """
    Given an array arr[] of N distinct elements and a number K, where K is smaller than
    the size of the array. Find the K'th smallest element in the given array.\n

    :param - arr (list of integers)\n
    :param - k (an integer)\n

    Retuns the k'th smallest element in the given array
    """
    # How I would implement this without using a heap
    kth = 0
    elems = []
    smallest_elem = arr[0]
    index = 0

    while kth < k:
        for i in range(len(arr)):
            if arr[i] < smallest_elem:
                smallest_elem = arr[i]
                index = i

        elems.append(smallest_elem)
        arr = arr[:index] + arr[index + 1 :]
        smallest_elem = arr[0]
        kth += 1

    return elems[k - 1]


def find_kth_smallest(arr: list[int], k: int) -> int:
    """
    Given an array arr[] of N distinct elements and a number K, where K is smaller than
    the size of the array. Find the K'th smallest element in the given array.\n

    :param - arr (list of integers)\n
    :param - k (an integer)\n

    Retuns the k'th smallest element in the given array
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

    return sorted_elems[-1]
