"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/min-heap-in-java/

Author: Nathan Lutala (nlutala)
"""


class MinHeap:
    """
    A Min-Heap is a complete binary tree in which the value in each internal
    node is smaller than or equal to the values in the children of that node.
    Mapping the elements of a heap into an array is trivial: if a node is
    stored an index k, then its left child is stored at index 2k + 1 and its
    right child at index 2k + 2.
    """

    def __init__(self, number=None) -> None:
        self.val = number
        self.left = None
        self.right = None
        self.minimum = None
        self.maximum = None
        self.nodes = []

        if self.val is not None:
            self.nodes.append(self.val)

    def getMin(self) -> int | None:
        """
        getMin(): It returns the root element of Min Heap. The Time Complexity
        of this operation is O(1).
        """
        return self.val

    def extractMin(self) -> int:
        """
        extractMin(): Removes the minimum element from MinHeap. The Time
        Complexity of this Operation is O(Log n) as this operation needs to
        maintain the heap property after removing the root.\n

        returns the minimum element in the MinHeap.
        """
        min_element = self.val

        if self.left.val <= self.right.val:
            temp_node = self.left
            self.val = self.left.val
            self.left = temp_node.left
        else:
            temp_node = self.right
            self.val = self.right.val
            self.right = temp_node.right

        self.nodes.remove(min_element)

        return min_element

    def insert(self, node: int) -> None:
        """
        insert(): Inserting a new key takes O(Log n) time. We add a new key at
        the end of the tree. If a new key is larger than its parent, then we
        don’t need to do anything. Otherwise, we need to traverse up to fix the
        violated heap property.\n

        :param - number (a MinHeap object)
        """
        if self.val is None:
            self.val = node
        elif self.val >= node:
            temp_node = self.val

            if self.left is None:
                self.val = node
                self.left = MinHeap(temp_node)
            else:
                self.val = node
                self.left.insert(temp_node)
        elif self.val < node:
            if self.right is None:
                self.right = MinHeap(node)
            else:
                self.right.insert(node)

        self.nodes.append(node)

    def __len__(self) -> int:
        """
        Overriding the len() method.
        """
        return len(self.nodes)
