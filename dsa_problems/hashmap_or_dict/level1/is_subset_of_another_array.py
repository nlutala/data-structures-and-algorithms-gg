"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/find-whether-an-array-is-subset-of-another-array-set-1/

Author: Nathan Lutala (nlutala)
"""


def is_subset(arr1: list[int], arr2: list[int]) -> bool:
    """
    Given two arrays arr1[] and arr2[] of size m and n respectively, the task
    is to determine whether arr2[] is a subset of arr1[]. Both arrays are not
    sorted, and elements are distinct.\n

    :param - arr1 (list of integers)\n
    :param - arr2 (list of integers)\n

    returns True (if it is a subset) or False (if not)
    """
    set_arr1 = set(arr1)
    set_arr2 = set(arr2)

    subset = set_arr1.intersection(set_arr2)

    return subset == set_arr2


if __name__ == "__main__":

    def test_is_subset_example_1():
        """
        Example 1:
        Input: arr1[] = {11, 1, 13, 21, 3, 7}, arr2[] = {11, 3, 7, 1}
        Output: True
        """
        arr1 = [11, 1, 13, 21, 3, 7]
        arr2 = [11, 3, 7, 1]

        return is_subset(arr1, arr2) is True

    def test_is_subset_example_2():
        """
        Example 2:
        Input: arr1[] = {1, 2, 3, 4, 5, 6}, arr2[] = {1, 2, 4}
        Output: True
        """
        arr1 = [1, 2, 3, 4, 5, 6]
        arr2 = [1, 2, 4]

        return is_subset(arr1, arr2) is True

    def test_is_subset_example_3():
        """
        Example 3:
        Input: arr1[] = {10, 5, 2, 23, 19}, arr2[] = {19, 5, 3}
        Output: False
        """
        arr1 = [10, 5, 2, 23, 19]
        arr2 = [19, 5, 3]

        return is_subset(arr1, arr2) is False

    print(
        test_is_subset_example_1(),
        test_is_subset_example_2(),
        test_is_subset_example_3(),
    )
