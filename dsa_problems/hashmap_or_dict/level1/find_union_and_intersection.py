"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/find-union-and-intersection-of-two-unsorted-arrays/

Author: Nathan Lutala (nlutala)
"""


def union_and_intersection(arr1: list[int], arr2: list[int]) -> list[list[int]]:
    """
    Given two unsorted arrays that represent two sets (elements in every array
    are distinct), find the union and intersection of two arrays.\n

    :param - arr1 (list of integers)\n
    :param - arr2 (list of integers)\n

    returns a list of lists (one list of the union, and another of the
    intersection).
    """
    union = sorted(list(set(arr1 + arr2)))
    intersection = [u for u in union if u in arr1 and u in arr2]

    return [union, intersection]


if __name__ == "__main__":

    def test_union_and_intersection():
        """
        Input : arr1[] = {7, 1, 5, 2, 3, 6}, arr2[] = {3, 8, 6, 20, 7}
        Output : Union : {1, 2, 3, 5, 6, 7, 8, 20}
        Intersection : {3, 6, 7}
        """
        arr1 = [7, 1, 5, 2, 3, 6]
        arr2 = [3, 8, 6, 20, 7]

        return union_and_intersection(arr1, arr2) == [
            [1, 2, 3, 5, 6, 7, 8, 20],
            [3, 6, 7],
        ]

    print(test_union_and_intersection())
