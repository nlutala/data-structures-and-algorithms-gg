"""
A file test the product function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.recursion.level2.product_of_two_numbers_using_recursion import product


def test_product_example_1():
    """
    Example 1:
    Input : x = 5, y = 2
    Output : 10
    """
    x, y = 5, 2
    assert product(x, y) == 10


def test_product_example_2():
    """
    Example 2:
    Input : x = 100, y = 5
    Output : 500
    """
    x, y = 100, 5
    assert product(x, y) == 500


# Custom tests
def test_product_example_3():
    """
    Example 3:
    Input : x = 100, y = -1
    Output : -100
    """
    x, y = 100, -1
    assert product(x, y) == -100


def test_product_example_4():
    """
    Example 4:
    Input : x = -50, y = -5
    Output : 250
    """
    x, y = -50, -5
    assert product(x, y) == 250


def test_product_example_5():
    """
    Example 4:
    Input : x = -4, y = 4
    Output : -16
    """
    x, y = -4, 4
    assert product(x, y) == -16
