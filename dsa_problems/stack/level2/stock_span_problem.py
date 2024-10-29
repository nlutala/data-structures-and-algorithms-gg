"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/the-stock-span-problem/

Author: Nathan Lutala (nlutala)
"""


def stock_span(n: int, prices: list[int]) -> list[int]:
    """
    The stock span problem is a financial problem where we have a series of N daily
    price quotes for a stock and we need to calculate the span of the stock’s price for
    all N days. The span Si of the stock’s price on a given day i is defined as the
    maximum number of consecutive days just before the given day, for which the price of
    the stock on the current day is less than or equal to its price on the given day.\n

    :param - n (an integer)\n
    :param - prices (a list of integers)\n

    Returns a list of integers denoting the stock span.
    """
    stock_span = []
    past_days = []

    for i in range(n):
        span = 1

        if past_days:
            # The stack part... kind of
            for j in range(len(past_days) - 1, -1, -1):
                if prices[i] > past_days[j]:
                    span += 1
                else:
                    break

        stock_span.append(span)
        past_days.append(prices[i])

    return stock_span
