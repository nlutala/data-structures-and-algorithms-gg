"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/mean-of-array-using-recursion/?

Author: Nathan Lutala (nlutala)
"""


def mean(arr: list[int], n: int) -> int | float:
    """
    You are given a list of integers arr. Return the mean (i.e. average) of
    the numbers in the array without the help of loops.\n

    :param - arr (the list of integers)\n
    :param - n (the number of elements in the array)\n

    Return the mean of the integers in arr.
    """
    # No idea how this works: Needs to be looked at further
    if n == 1:
        return arr[n - 1]
    else:
        return (mean(arr, n - 1) * (n - 1) + arr[n - 1]) / n


if __name__ == "__main__":

    def test_mean_example_1():
        """
        Example 1:
        Input : [1, 2, 3, 4, 5]
        Output : 3
        """
        arr = [1, 2, 3, 4, 5]
        n = 5
        print(mean(arr, n))
        return mean(arr, n) == 3

    def test_mean_example_2():
        """
        Example 1:
        Input : [1, 2, 3]
        Output : 2
        """
        arr = [1, 2, 3]
        n = 3
        print(mean(arr, n))
        return mean(arr, n) == 2

    print(test_mean_example_1(), test_mean_example_2())
