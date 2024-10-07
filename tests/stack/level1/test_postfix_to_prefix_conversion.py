"""
A file tests the postfix_to_prefix function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.stack.level1.postfix_to_prefix_conversion import postfix_to_prefix


def test_postfix_to_prefix_example_1():
    """
    Example 1:
    Input :  Postfix : AB+CD-*
    Output : Prefix :  *+AB-CD
    Explanation : Postfix to Infix : (A+B) * (C-D)
    Infix to Prefix :  *+AB-CD
    """
    exp = "AB+CD-*"
    return postfix_to_prefix(exp) == "*+AB-CD"


def test_postfix_to_prefix_example_2():
    """
    Example 2:
    Input :  Postfix : ABC/-AK/L-*
    Output : Prefix :  *-A/BC-/AKL
    Explanation : Postfix to Infix : ((A-(B/C))*((A/K)-L))
    Infix to Prefix :  *-A/BC-/AKL
    """
    exp = "ABC/-AK/L-*"
    return postfix_to_prefix(exp) == "*-A/BC-/AKL"
