"""
A file test the delete_linked_list function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.recursion.level2.delete_a_linked_list_using_recursion import (
    LinkedList,
    delete_linked_list,
)


def test_delete_linked_list_example_1():
    """
    Example 1:
    Input: Linked List = 1 -> 2 -> 3 -> 4 -> 5 -> NULL
    Output:  NULL
    Explanation:  Linked List is Deleted
    """
    # Create a hard-coded linked list:
    # 1 -> 2 -> 3 -> 4 -> 5
    head = LinkedList(1)
    head.next = LinkedList(2)
    head.next.next = LinkedList(3)
    head.next.next.next = LinkedList(4)
    head.next.next.next.next = LinkedList(5)
    assert delete_linked_list(head) is None

    # Check that the linked_list is really deleted
    assert head.data is None
    assert head.next is None


def test_delete_linked_list_example_2():
    """
    Example 2:
    Input: Linked List = 1 -> 12 -> 1 -> 4 -> 1 -> NULL
    Output: NULL
    Explanation:  Linked List is Deleted
    """
    # Create a hard-coded linked list:
    # 1 -> 12 -> 1 -> 4 -> 1 -> NULL
    head = LinkedList(1)
    head.next = LinkedList(12)
    head.next.next = LinkedList(1)
    head.next.next.next = LinkedList(4)
    head.next.next.next.next = LinkedList(1)
    assert delete_linked_list(head) is None

    # Check that the linked_list is really deleted
    assert head.data is None
    assert head.next is None
