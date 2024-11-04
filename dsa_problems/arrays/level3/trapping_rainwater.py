"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/trapping-rain-water/

Author: Nathan Lutala (nlutala)
"""


def get_rainwater_collected(arr: list[int]) -> int:
    """
    Trapping Rainwater Problem states that given an array of n non-negative integers
    arr[] representing an elevation map where the width of each bar is 1, compute how
    much water it can trap after rain.\n

    :param - arr (list of integers)\n

    returns the number of the number x in the array
    """
    rainwater_collected = 0

    if arr.count(0) != 0:
        second_tallest = sorted(arr, reverse=True)[1]

        for i in range(len(arr)):
            if max(sorted(arr[i:], reverse=True)) >= second_tallest:
                if arr[i] <= second_tallest:
                    rainwater_collected += second_tallest - arr[i]
            else:
                second_tallest = sorted(arr[i:], reverse=True)[0]
                rainwater_collected += second_tallest - arr[i]

            print(rainwater_collected, arr[i:])

    return rainwater_collected
