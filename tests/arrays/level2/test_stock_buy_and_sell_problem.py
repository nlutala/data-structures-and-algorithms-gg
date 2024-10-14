"""
A file tests the stock_buy_sell function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.arrays.level2.stock_buy_and_sell_problem import stock_buy_sell


def test_stock_buy_sell_example_1():
    """
    Example 1:
    Input: prices[] = {100, 180, 260, 310, 40, 535, 695}
    Output: 865
    Explanation: Buy the stock on day 0 and sell it on day 3 => 310 – 100 = 210
                       Buy the stock on day 4 and sell it on day 6 => 695 – 40 = 655
                       Maximum Profit  = 210 + 655 = 865
    """
    prices = [100, 180, 260, 310, 40, 535, 695]
    assert stock_buy_sell(prices) == 865


def test_stock_buy_sell_example_2():
    """
    Example 2:
    Input: prices[] = {4, 2, 2, 2, 4}
    Output: 2
    Explanation: Buy the stock on day 4 and sell it on day 5 => 4 – 2 = 2
                 Maximum Profit  = 2
    """
    prices = [4, 2, 2, 2, 4]
    assert stock_buy_sell(prices) == 2


# Custom tests
def test_stock_buy_sell_example_3():
    """
    Example 3:
    Input: prices[] = {2, 3, 4, 1, 10, 9, 11}
    Output: 12
    """
    prices = [2, 3, 4, 1, 10, 9, 11]
    assert stock_buy_sell(prices) == 12


def test_stock_buy_sell_example_4():
    """
    Example 4:
    Input: prices[] = {2, 1, 10, 9, 11}
    Output: 10
    """
    prices = [2, 1, 10, 9, 11]
    assert stock_buy_sell(prices) == 10


def test_stock_buy_sell_example_5():
    """
    Example 5:
    Input: prices[] = {2, 1, 3, 10, 9, 5}
    Output: 8
    """
    prices = [2, 1, 3, 10, 9, 5]
    assert stock_buy_sell(prices) == 9
