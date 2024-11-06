"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/find-pairs-b-array-b-k/

Author: Nathan Lutala (nlutala)
"""


def find_pairs_a_modulo_b(arr: list[int], k: int) -> list[tuple[int, int]] | None:
    """
    Given an array with distinct elements, the task is to find the pairs in the array
    such that a % b = k, where k is a given integer. You may assume that a and b are in
    small range.\n

    :param - arr (list of integers)\n
    :param - k (integer)\n

    returns the pairs in which the modulo of them are equal to k.
    """
    pairs = []

    for i, num in enumerate(arr):
        arr_without = [arr[j] for j in range(len(arr)) if i != j]
        for l in range(len(arr_without)):
            if num % arr_without[l] == k:
                if (num, arr_without[l]) not in pairs:
                    pairs.append((num, arr_without[l]))

            if arr_without[l] % num == k:
                if (arr_without[l], num) not in pairs:
                    pairs.append((arr_without[l], num))

    print(pairs)

    return None if len(pairs) == 0 else pairs
