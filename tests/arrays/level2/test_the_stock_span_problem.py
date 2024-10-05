"""
A file tests the stock_span function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.arrays.level2.the_stock_span_problem import stock_span


def test_stock_span_example_1():
    """
    Example 1:
    Input: N = 7, price[] = [100 80 60 70 60 75 85]
    Output: 1 1 1 2 1 4 6
    Explanation:
    Traversing the given input span for 100 will be 1, 80 is
    smaller than 100 so the span is 1, 60 is smaller than 80 so the span is 1,
    70 is greater than 60 so the span is 2 and so on. Hence the output will be
    1 1 1 2 1 4 6.
    """
    n = 7
    price = [100, 80, 60, 70, 60, 75, 85]

    assert stock_span(n, price) == [1, 1, 1, 2, 1, 4, 6]


def test_stock_span_example_2():
    """
    Example 2:
    Input: N = 6, price[] = [10 4 5 90 120 80]
    Output:1 1 2 4 5 1
    Explanation: Traversing the given input span for 10 will be 1, 4 is
    smaller than 10 so the span will be 1, 5 is greater than 4 so the span
    will be 2 and so on. Hence, the output will be 1 1 2 4 5 1.
    """
    n = 6
    price = [10, 4, 5, 90, 120, 80]

    assert stock_span(n, price) == [1, 1, 2, 4, 5, 1]
