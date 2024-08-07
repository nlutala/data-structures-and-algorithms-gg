"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/count-pairs-with-given-sum/

Author: Nathan Lutala (nlutala)
"""


def count_pairs_with_sum(arr: list, k: int) -> list[list[int]]:
    """
    Given an array of N integers, and an integer K, the task is to find the
    number of pairs of integers in the array whose sum is equal to K. \n

    :param - arr (list)\n

    returns a list with the pairs that add up to the sum.
    """
    new_array = arr.copy()
    pairs = []
    freq_num = {}

    for num in new_array:
        if k - num in new_array:
            pairs.append(sorted([k - num, num]))

        if freq_num.get(str(num)) is None:
            freq_num[str(num)] = 1
        else:
            freq_num[str(num)] = freq_num.get(str(num)) + 1

    for i, pair in enumerate(pairs):
        total_in_pairs = pairs.count(pair)
        total_of_pair_1 = freq_num.get(str(pair[0]))
        total_of_pair_2 = freq_num.get(str(pair[1]))
        if total_in_pairs > total_of_pair_1:
            if total_in_pairs > total_of_pair_2:
                pairs.remove(pair)

    return len(pairs)
