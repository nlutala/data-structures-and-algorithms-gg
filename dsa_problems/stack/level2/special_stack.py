"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/design-and-implement-special-stack-data-structure/

Author: Nathan Lutala (nlutala)
"""


class SpecialStack:
    """
    Design a Data Structure SpecialStack that supports all the stack operations like
    push(), pop(), isEmpty(), isFull() and an additional operation getMin() which should
    return minimum element from the SpecialStack. All these operations of SpecialStack
    must be O(1). To implement SpecialStack, you should only use standard Stack data
    structure and no other data structure like arrays, list, . etc.
    """

    def __init__(self, max_size=10) -> None:
        self.elements = []
        self.max_size = max_size

    def push(self, element: int) -> None:
        """
        Adds an element to the top of the stack. (Inserted at index 0)\n

        :param - element (integer)
        """
        if len(self.elements) < self.max_size:
            self.elements.insert(0, element)
        else:
            raise MemoryError(
                f"""Maximum size of {self.max_size} elements has been reached."""
            )

    def pop(self) -> int | None:
        """
        Removes the element at the top of the stack.\n

        Returns an integer (or None if there are no elements in the SpecialStack).
        """
        if self.elements:
            return self.elements.pop(0)

    def isEmpty(self) -> bool:
        """
        Returns True if the SpecialStack is empty, and False if otherwise.
        """
        return len(self.elements) == 0

    def isFull(self) -> bool:
        """
        Returns True if the SpecialStack has reached it's max size, and False if
        otherwise.
        """
        return len(self.elements) == self.max_size

    def getMin(self) -> int | None:
        """
        Returns the smallest element in the SpecialStack, and None if there are no
        elements in the SpecialStack.
        """
        return min(self.elements)
