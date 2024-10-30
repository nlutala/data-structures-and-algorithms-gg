"""
A file tests the TwoStacks class

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.arrays.level2.implement_two_stacks_in_an_array import (
    TwoStacks,
)


def test_TwoStacks_example_1():
    """
    Example 1:
    Input: push_to_stack_1 = [5, 11], push_to_stack_2 = [10, 15, 7]
    Pop element from stack 1 (should be 11)
    Pop element from stack 2 (should be 7)
    """
    ts = TwoStacks()

    ts.push1(5)
    ts.push2(10)
    ts.push2(15)
    ts.push1(11)
    ts.push2(7)

    assert ts.pop1() == 11
    assert ts.pop2() == 7


def test_TwoStacks_example_2():
    """
    Example 2:
    Input: push_to_stack_1 = [5, 11], push_to_stack_2 = [10, 15, 7]
    Pop element from stack 1 (should be 11)
    Pop element from stack 2 (should be 7)
    """
    ts = TwoStacks(5)

    ts.push1(5)
    ts.push2(10)
    ts.push2(15)
    ts.push1(11)
    ts.push2(7)
    ts.push2(40)

    assert ts.pop1() == 11
    assert ts.pop2() == 40


def test_TwoStacks_example_3():
    """
    Example 3:
    Input: to_stack_1 = [5, 11], to_stack_2 = [10, 15, 7, 40, 8, 9, 1]
    Pop element from stack 1 (should be 11)
    Pop element from stack 2 (should be 7)
    Add 8, 9 and 1 to stack 2 (should return a string saying max size
    reached)
    Pop element from stack 2 (should be 1)
    """
    ts = TwoStacks(5)

    ts.push1(5)
    ts.push2(10)
    ts.push2(15)
    ts.push1(11)
    ts.push2(7)
    ts.push2(40)

    assert ts.pop1() == 11
    assert ts.pop2() == 40

    ts.push2(8)
    ts.push2(9)

    assert ts.push2(1) == "The max size of the second stack has been reached."

    assert ts.pop2() == 9
