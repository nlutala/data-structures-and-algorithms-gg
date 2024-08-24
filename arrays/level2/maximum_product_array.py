"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/maximum-product-subarray/

Author: Nathan Lutala (nlutala)
"""


def max_product(array: list[int]) -> int:
    """
    Given an array that contains both positive and negative integers, the task
    is to find the product of the maximum product subarray.\n

    :param - array (list of integers)\n

    returns the maximum product of a subarray in the array.
    """
    # Find the largest number in the array as a baseline
    max_product_subarray = max(array)

    # Start with a subarray of length 2 (if possible)
    end = 2

    def get_produt_of_array(arr: list[int]):
        """
        An inner function to help get the product of the integers in an array.
        \n
        :param - array (list of integers)\n

        returns the product of an array.
        """
        product = 1

        for num in arr:
            product *= num

        return product

    while end != len(array):
        for i in range(len(array)):
            product = get_produt_of_array(array[i:end])

            if product > max_product_subarray:
                max_product_subarray = product

        end += 1

    return max_product_subarray
