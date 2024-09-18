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

    # Get the frequencies of each number as a dictionary {occurences: [number]}
    freq_dict = {}

    for a in arr_set:
        if freq_dict.get(str(arr.count(a))) is None:
            freq_dict[str(arr.count(a))] = [a]
        else:
            freq_dict[str(arr.count(a))] = sorted(freq_dict.get(
                str(arr.count(a))
            ) + [a], reverse=True)

    occurrences = []

    for key in freq_dict:
        occurrences = freq_dict.get(key) + occurrences

    return occurrences[:k]
