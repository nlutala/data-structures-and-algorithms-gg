"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/priority-queue-set-1-introduction/

Author: Nathan Lutala (nlutala)
"""


class PriorityQueue:
    """
    A priority queue is a type of queue that arranges elements based on their priority
    values. Elements with higher priority values are typically retrieved or removed
    before elements with lower priority values. Each element has a priority value
    associated with it. When we add an item, it is inserted in a position based on its
    priority value.
    """

    def __init__(self) -> None:
        """
        Constructor for the PriorityQueue object.
        """
        self.elements = []

    def insert(self, element: tuple[int, int]) -> None:
        """
        When a new element is inserted in a priority queue, it moves to the empty slot
        from top to bottom and left to right. However, if the element is not in the
        correct place then it will be compared with the parent node. If the element is
        not in the correct order, the elements are swapped. The swapping process
        continues until all the elements are placed in the correct position.\n

        :param - element (tuple)\n

        Returns None.
        """
        elements_before = self.elements

        if self.elements:
            for i, elem in enumerate(self.elements):
                if elem[1] > element[1]:
                    self.elements.insert(i, element)
                    break

        if elements_before == self.elements:
            self.elements.append(element)

    def delete(self) -> tuple[int, int] | None:
        """
        As you know that in a max heap, the maximum element is the root node. And it
        will remove the element which has maximum priority first. Thus, you remove the
        root node from the queue. This removal creates an empty slot, which will be
        further filled with new insertion. Then, it compares the newly inserted element
        with all the elements inside the queue to maintain the heap invariant.\n

        Returns the maximum in the priority queue.
        """
        if self.elements:
            return self.elements.pop(0)[0]

        # return None (done implicitly)

    def peek(self) -> tuple[int, int] | None:
        """
        This operation helps to return the maximum element from Max Heap or the minimum
        element from Min Heap without deleting the node from the priority queue.\n

        Returns the maximum element from the priority queue without deleteing it.
        """
        if self.elements:
            return self.elements[0][0]

        # return None (done implicitly)
