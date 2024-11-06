"""
A file tests the PriorityQueue class

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.heaps.level2.implement_a_priority_queue import PriorityQueue


def test_PriorityQueue_example_1():
    """
    Example 1:
    Input: (10, 2), (14, 4), (16, 4), (12, 3)
    Output:
    * Peek - 10
    * Delete - 10
    * Peek - 12
    * Delete - 12
    * Peek - 14
    """
    # elements: list[tuple[int (element), int (priority)]]
    elements = [(10, 2), (14, 4), (16, 4), (12, 3)]
    pq = PriorityQueue()

    for elem in elements:
        pq.insert(elem)

    assert pq.peek() == 10
    assert pq.delete() == 10
    assert pq.peek() == 12
    assert pq.delete() == 12
    assert pq.peek() == 14


def test_PriorityQueue_example_2():
    """
    Example 2:
    Input: (4, 1), (5, 2), (6, 3), (7, 0)
    Output:
    * Peek - 7
    * Delete - 7
    * Peek - 4
    * Delete - 4
    * Peek - 5
    """
    # elements: list[tuple[int (element), int (priority)]]
    elements = [(4, 1), (5, 2), (6, 3), (7, 0)]
    pq = PriorityQueue()

    for elem in elements:
        pq.insert(elem)

    assert pq.peek() == 7
    assert pq.delete() == 7
    assert pq.peek() == 4
    assert pq.delete() == 4
    assert pq.peek() == 5
