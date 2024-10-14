"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/stock-buy-sell/

Author: Nathan Lutala (nlutala)
"""


def stock_buy_sell(prices: list[int]) -> int:
    """
    Given an array prices[] of size n denoting the cost of stock on each day, the task
    is to find the maximum total profit if we can buy and sell the stocks any number of
    times.\n

    Note: We can only sell a stock which we have bought earlier and we cannot hold
    multiple stocks on any day.\n

    :param - arr (list of integers)\n

    returns the maximum total profit if we can buy and sell the stocks any number of
    times.
    """
    max_profit = 0
    last_price = 0
    window = []

    for i in range(len(prices)):
        if i == 0:
            if prices[i] < prices[i + 1]:
                last_price = prices[i]
            else:
                last_price = prices[i + 1]
        else:
            if prices[i] >= last_price:
                window.append(prices[i])
            else:
                max_profit += max(window) - last_price
                last_price = prices[i]
                window = []

    if len(window) > 0:
        max_profit += max(window) - last_price

    return max_profit
