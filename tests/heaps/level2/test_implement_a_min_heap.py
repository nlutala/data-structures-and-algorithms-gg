"""
A file tests the MinHeap class

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.heaps.level2.implement_a_min_heap import MinHeap


def test_height_of_tree_example_1():
    """
    Example 1:
    Input : [5, 3, 17, 10, 84, 19, 6, 22, 9]
    Output :
    PARENT : 3 LEFT CHILD : 5 RIGHT CHILD :6
    PARENT : 5 LEFT CHILD : 9 RIGHT CHILD :84
    PARENT : 6 LEFT CHILD : 19 RIGHT CHILD :17
    PARENT : 9 LEFT CHILD : 22 RIGHT CHILD :10
    The Min val is 3
    """
    minheap = MinHeap()
    nodes_to_insert = [5, 3, 17, 10, 84, 19, 6, 22, 9]

    # Insert nodes into the MinHeap
    for node in nodes_to_insert:
        minheap.insert(node)

    # Assert that the number of nodes inserted is the same as the number of nodes in
    # the nodes_to_insert list
    assert len(minheap) == len(nodes_to_insert)

    # Assert that the smallest element in the MinHeap is 3
    assert minheap.extractMin() == 3

    # After removing extracting the minimum, there should be 1 less element
    assert len(minheap) == len(nodes_to_insert) - 1
