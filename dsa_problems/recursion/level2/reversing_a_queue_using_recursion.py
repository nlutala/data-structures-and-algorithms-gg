"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/reversing-queue-using-recursion/

Author: Nathan Lutala (nlutala)
"""


def reverse_queue(queue: list) -> list:
    """
    Given a queue, write a recursive function to reverse it.\n

    enqueue(x) : Add an item x to rear of queue.\n
    dequeue() : Remove an item from front of queue.\n
    empty() : Checks if a queue is empty or not.\n

    :param - queue (a a string)\n

    returns the reversed queue.
    """
    # I had help from the guidelines below:
    # Recursive Algorithm :
    # The pop element from the queue if the queue has elements otherwise return empty queue.
    # Call reverseQueue function for the remaining queue.
    # Push the popped element in the resultant reversed queue.

    if len(queue) <= 1:
        return queue
    else:
        return reverse_queue(queue[1:]) + [queue[0]]
