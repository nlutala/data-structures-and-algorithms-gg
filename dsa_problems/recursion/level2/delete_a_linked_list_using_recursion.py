"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/delete-linked-list-using-recursion/

Author: Nathan Lutala (nlutala)
"""


class LinkedList:
    """
    An object defining a linked list.\n

    It is initialised by supplying new_data (an integer).
    """

    def __init__(self, new_data: int):
        self.data = new_data
        self.next = None


def delete_linked_list(linked_list: object) -> None:
    """
    Given a linked list, the task is to delete the linked list using 
    recursion.\n

    :param - linked_list (a LinkedList object)\n

    returns the resulting linked_list (should be None).
    """
    if linked_list is None:
        return linked_list

    linked_list.data = None
    next_linked_list = linked_list.next
    linked_list.next = None
    return delete_linked_list(next_linked_list)
