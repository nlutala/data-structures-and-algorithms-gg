"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/find-a-repeating-and-a-missing-number/

Author: Nathan Lutala (nlutala)
"""


def get_missing_and_repating(arr: list[int]) -> list[int]:
    """
    Given an unsorted array of size n. Array elements are in the range of 1 to
    n. One number from set {1, 2, …n} is missing and one number occurs twice
    in the array. Find these two numbers.\n

    :param - arr (list of integers)\n

    returns a list with the pairs that add up to the sum.
    """
    missing = None
    repeating = None

    # Find the missing number
    minimum = None
    maximum = None

    for num in arr:
        if minimum is None:
            minimum = num
        else:
            if minimum > num:
                minimum = num

        if maximum is None:
            maximum = num
        else:
            if maximum < num:
                maximum = num

    missing_numbers = [i for i in range(minimum, maximum + 1) if i not in arr]

    if len(missing_numbers) > 0:
        missing = missing_numbers[0]

    # Find the repeating number
    set_arr = list(set(arr))
    number_occurrences = {}
    occurrences = 0

    for num in set_arr:
        for elem in arr:
            if elem == num:
                occurrences += 1

        number_occurrences[str(num)] = occurrences
        occurrences = 0

    for number in number_occurrences:
        if number_occurrences.get(number) > 1:
            repeating = int(number)
        
    return [missing, repeating]
