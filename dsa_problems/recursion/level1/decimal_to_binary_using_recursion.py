"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/decimal-binary-number-using-recursion/

Author: Nathan Lutala (nlutala)
"""


def decimal_to_binary(number: int) -> str:
    """
    Given a decimal number as input, we need to write a program to convert the given
    decimal number into an equivalent binary number.\n

    :param - number (a positive integer)\n

    Return the binary representation of the integer.
    """
    # Incoherent code but I'm hoping it makes sense with the comments

    # Return 0 if the number is 0
    if number == 0:
        return "0"
    # Return 1 if the number is 1
    elif number == 1:
        return "1"
    else:
        # Step 1. Get the power of two, x, in which 2^x <= number
        power_of_two = 0

        while 2**power_of_two <= number:
            power_of_two += 1

        power_of_two -= 1

        # Step 2. Try to get the next power of 2 for the new number (number - 2^x) by
        # doing step 1 again.
        new_power_of_two = power_of_two

        while 2**new_power_of_two > number - 2**power_of_two:
            new_power_of_two -= 1

        new_power_of_two += 1

        # Step 3a. If the number - 2^x is greater than 0, add padding of the zeros (if
        # needed)
        if number - (2**power_of_two) > 0:
            return (
                "1"
                + ("0" * (power_of_two - new_power_of_two))
                + decimal_to_binary(number - (2**power_of_two))
            )

        # Step 3b. If the number - 2^x is 0, add padding of x - 1
        return (
            "1"
            + ("0" * (power_of_two - 1))
            + decimal_to_binary(number - (2**power_of_two))
        )
