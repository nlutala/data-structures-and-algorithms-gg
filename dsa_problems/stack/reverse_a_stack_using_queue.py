"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/reverse-a-stack-using-queue/

Author: Nathan Lutala (nlutala)
"""


def reverse_stack(stack: list) -> list:
    """
    Given a stack, the task is to reverse the stack using the queue data
    structure.\n

    :param - postfix_exp (the postfix expression)\n

    Return the prefix expression string.
    """
    queue = []
    new_stack = []

    for i in range(len(stack)):
        queue.append(stack.pop())

    for q in queue:
        new_stack.insert(0, q)

    return new_stack
