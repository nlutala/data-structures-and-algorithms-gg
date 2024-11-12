"""
A file tests the SpecialStack object

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.stack.level2.special_stack import SpecialStack


def test_special_stack():
    """
    Consider the following SpecialStack
    16  --> TOP
    15
    29
    19
    18

    When getMin() is called it should
    return 15, which is the minimum
    element in the current stack.

    If we do pop two times on stack,
    the stack becomes
    29  --> TOP
    19
    18

    When getMin() is called, it should
    return 18 which is the minimum in
    the current stack.
    """
    elements = [18, 19, 29, 15, 16]
    ss = SpecialStack()

    for e in elements:
        ss.push(e)

    assert ss.getMin() == 15

    ss.pop()
    ss.pop()

    assert 16 not in ss.elements and 15 not in ss.elements

    assert ss.getMin() == 18
