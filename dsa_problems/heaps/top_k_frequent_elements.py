"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/find-k-numbers-occurrences-given-array/

Author: Nathan Lutala (nlutala)
"""


def frequent_elements(arr: list[int], k: int) -> list[int]:
    """
    Given an array of n numbers and a positive integer K. The problem is to
    find K numbers with the most occurrences. If two numbers have the same
    frequency then the number with a larger value should be given preference.
    The numbers should be displayed in decreasing order of their frequencies.
    It is assumed that the array consists of at least K numbers.\n

    :param - arr (list of integers)\n
    :param - k (integer, k numbers with the most occurrences)\n

    Returns K numbers with the most occurrences
    """
    arr_set = list(set(arr))
    freq_dict = {}

    for a in arr_set:
        count_key = str(arr.count(a))
        if freq_dict.get(count_key) is None:
            freq_dict[count_key] = [a]
        else:
            freq_dict[count_key] = freq_dict.get(count_key) + [a]

    freq_keys = sorted(list(freq_dict.keys()), reverse=True)

    freq_elems = []

    for key in freq_keys:
        freq_elems += sorted(freq_dict.get(key), reverse=True)

    return freq_elems[:k]
