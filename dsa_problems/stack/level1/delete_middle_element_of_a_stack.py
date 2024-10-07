"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/delete-middle-element-stack/

Author: Nathan Lutala (nlutala)
"""


def remove_middle_elem(stack: list) -> list:
    """
    Given a stack with push(), pop(), and empty() operations, The task is to
    delete the middle element of it without using any additional data.\n

    :param - string1 (a string)\n
    :param - string2 (a string)\n

    Return a new stack with the middle element removed.
    """
    middle = int(len(stack) / 2)

    # The middle changes slightly based on whether the size of the stack is
    # even or odd
    if len(stack) % 2 == 0:
        middle -= 1

    final_stack = []
    temp_stack = []

    while len(temp_stack) != middle:
        temp_stack.insert(0, stack[0])
        stack = stack[1:]
    stack = stack[1:]

    # Imagine I'm popping the remaining elements from stack into another stack
    # called reversed_stack
    reversed_stack = [stack[i] for i in range(len(stack) - 1, -1, -1)]

    while len(reversed_stack) != 0 or len(temp_stack) != 0:
        if len(reversed_stack) != 0:
            final_stack.insert(0, reversed_stack[0])
            reversed_stack = reversed_stack[1:]
        else:
            final_stack.insert(0, temp_stack[0])
            temp_stack = temp_stack[1:]

    return final_stack
