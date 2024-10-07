"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/top-50-problems-on-heap-data-structure-asked-in-interviews/

Author: Nathan Lutala (nlutala)
"""


def min_sum(arr: list[int]) -> int:
    """
    Given an array of digits (values are from 0 to 9), find the minimum
    possible sum of two numbers formed from digits of the array. All digits of
    given array must be used to form the two numbers.\n

    :param - arr (a list of integers)\n

    Returns the smallest sum that can be made from the list.
    """
    # Sort the list in heap style fashion
    sorted_arr = []

    for a in arr:
        if len(sorted_arr) == 0:
            sorted_arr.append(a)
        else:
            less_than = [num for num in sorted_arr if num <= a]
            greater_than = [num for num in sorted_arr if num > a]
            sorted_arr = less_than + [a] + greater_than

    # Go through the sorted list and alternate the numbers into two lists
    num1 = ""
    num2 = ""

    for i in range(len(sorted_arr)):
        if i % 2 == 0:
            num1 += str(sorted_arr[i])
        else:
            num2 += str(sorted_arr[i])

    if num1[0] == "0":
        num1 = num1[1:]

    if num2[0] == "0":
        num2 = num2[1:] 

    # Return the sum of the two numbers
    return int(num1) + int(num2)
