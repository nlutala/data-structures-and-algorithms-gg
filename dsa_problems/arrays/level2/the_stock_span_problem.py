"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/the-stock-span-problem/

Author: Nathan Lutala (nlutala)
"""


def stock_span(n: int, prices: list[int]) -> list[int]:
    """
    The stock span problem is a financial problem where we have a series of N
    daily price quotes for a stock and we need to calculate the span of the
    stock’s price for all N days. The span Si of the stock’s price on a given
    day i is defined as the maximum number of consecutive days just before the
    given day, for which the price of the stock on the current day is less
    than or equal to its price on the given day.
    """
    result = []

    for i in range(len(prices)):
        window = prices[0 : i + 1]

        if len(window) == 1:
            result.append(1)
        else:
            span_found = False
            while span_found is False:
                if max(window) == prices[i]:
                    span_found = True
                    result.append(len(window))
                else:
                    window = window[1:]

    return result
