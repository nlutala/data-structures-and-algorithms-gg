"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/implement-two-stacks-in-an-array/

Author: Nathan Lutala (nlutala)
"""
import sys


class TwoStacks:
    """
    Create a data structure twoStacks that represent two stacks.
    Implementation of twoStacks should use only one array, i.e., both stacks
    should use the same array for storing elements.
    """

    def __init__(self, size=sys.maxsize) -> None:
        """
        TwoStacks constructor.\n

        :param - size (int, the fixed size of the two stacks - this is
        optional, leave unspecified if you want to work with fully dynamic
        stacks)
        """
        self.array = [[], []]
        self.size = size

    def push1(self, x: int) -> str | None:
        """
        Pushes x to the first stack.\n

        :param - x (an integer)
        """
        if len(self.array[0]) < self.size:
            self.array[0].insert(0, x)
        else:
            return "The max size of the first stack has been reached."

    def push2(self, x: int) -> str | None:
        """
        Pushes x to the second stack.\n

        :param - x (an integer)
        """
        if len(self.array[1]) < self.size:
            self.array[1].insert(0, x)
        else:
            return "The max size of the second stack has been reached."

    def pop1(self) -> int | str:
        """
        Pops an element from first stack and return the popped element
        """
        if self.array[0]:
            return self.array[0].pop(0)
        else:
            return "No elements found in the first stack"

    def pop2(self) -> int | str:
        """
        Pops an element from second stack and return the popped element
        """
        if self.array[0]:
            return self.array[1].pop(0)
        else:
            return "No elements found in the second stack"
