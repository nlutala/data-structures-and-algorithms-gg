"""
A file tests the MaxHeap class

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.heaps.level2.implement_a_max_heap import MaxHeap


def test_height_of_tree_example_1():
    """
    Example 1:
    Input : [5, 3, 17, 10, 84, 19, 6, 22, 9]
    Output :
    PARENT: 84 LEFT CHILD: 22 RIGHT CHILD: 19
    PARENT: 22 LEFT CHILD: 17 RIGHT CHILD: 10
    PARENT: 19 LEFT CHILD: 5 RIGHT CHILD: 6
    PARENT: 17 LEFT CHILD: 3 RIGHT CHILD: 9
    The Max val is 84
    """
    maxheap = MaxHeap()
    nodes_to_insert = [5, 3, 17, 10, 84, 19, 6, 22, 9]

    # Insert nodes into the MaxHeap
    for node in nodes_to_insert:
        maxheap.insert(node)

    # Assert that the number of nodes inserted is the same as the number of nodes in
    # the nodes_to_insert list
    assert len(maxheap) == len(nodes_to_insert)


def test_height_of_tree_example_2():
    """
    Example 2 (Example 1 continued):
    Input : [5, 3, 17, 10, 84, 19, 6, 22, 9]
    Output :
    PARENT: 84 LEFT CHILD: 22 RIGHT CHILD: 19
    PARENT: 22 LEFT CHILD: 17 RIGHT CHILD: 10
    PARENT: 19 LEFT CHILD: 5 RIGHT CHILD: 6
    PARENT: 17 LEFT CHILD: 3 RIGHT CHILD: 9
    The Max val is 84
    """
    maxheap = MaxHeap()
    nodes_to_insert = [5, 3, 17, 10, 84, 19, 6, 22, 9]

    # Insert nodes into the MaxHeap
    for node in nodes_to_insert:
        maxheap.insert(node)

    # Assert that the greatest element in the MaxHeap is 84
    assert maxheap.extractMax() == 84

    # After removing extracting the minimum, there should be 1 less element
    assert len(maxheap) == len(nodes_to_insert) - 1

    # The max should now be 22
    assert maxheap.getMax() == 22
