"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/longest-alternating-subsequence/

Author: Nathan Lutala (nlutala)
"""


def length_of_longest_subsequence(arr: list[int]) -> int:
    """
    A sequence {X1, X2, .. Xn} is an alternating sequence if its elements
    satisfy one of the following relations:\n

    X1 < X2 > X3 < X4 > X5 < …. xn or\n
    X1 > X2 < X3 > X4 < X5 > …. xn\n

    :param - arr (list of integers)\n

    returns the length of the longest_alternating subsequence in the list.
    """
    # Doing < then >
    less_than = True
    list1 = []

    # Doing > then <
    greater_than = True
    list2 = []

    for i in range(1, len(arr)):
        if len(list1) == 0:
            if less_than:
                if arr[i - 1] < arr[i]:
                    list1.append(arr[i - 1])
                    list1.append(arr[i])
                    less_than = False
        else:
            if less_than:
                if list1[-1] < arr[i]:
                    list1.append(arr[i])
                    less_than = False
            else:
                if list1[-1] > arr[i]:
                    list1.append(arr[i])
                    less_than = True

        if len(list2) == 0:
            if greater_than:
                if arr[i - 1] > arr[i]:
                    list2.append(arr[i - 1])
                    list2.append(arr[i])
                    greater_than = False
        else:
            if greater_than:
                if list2[-1] > arr[i]:
                    list2.append(arr[i])
                    greater_than = False
            else:
                if list2[-1] < arr[i]:
                    list2.append(arr[i])
                    greater_than = True

    return max([len(list1), len(list2)])
