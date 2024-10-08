"""
A file test the reverse_queue function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.recursion.level2.reversing_a_queue_using_recursion import (
    reverse_queue,
)


def test_reverse_queue_example_1():
    """
    Example 1:
    Input : Q = [5, 24, 9, 6, 8, 4, 1, 8, 3, 6]
    Output : Q = [6, 3, 8, 1, 4, 8, 6, 9, 24, 5]
    Explanation : Output queue is the reverse of the input queue.
    """
    Q = [5, 24, 9, 6, 8, 4, 1, 8, 3, 6]
    assert reverse_queue(Q) == [6, 3, 8, 1, 4, 8, 6, 9, 24, 5]


def test_reverse_queue_example_2():
    """
    Example 2:
    Input : Q = [8, 7, 2, 5, 1]
    Output : Q = [1, 5, 2, 7, 8]
    """
    Q = [8, 7, 2, 5, 1]
    assert reverse_queue(Q) == [1, 5, 2, 7, 8]


# Custom tests
def test_reverse_queue_example_3():
    """
    Example 3:
    Input : Q = []
    Output : Q = []
    """
    Q = []
    assert reverse_queue(Q) == []


def test_reverse_queue_example_4():
    """
    Example 4:
    Input : Q = [1]
    Output : Q = [1]
    """
    Q = [1]
    assert reverse_queue(Q) == [1]
