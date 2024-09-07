"""
A file tests the find_factorial function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.arrays.level2.find_the_factorial_of_a_larger_number import find_factorial


def test_find_factorial_example_1():
    """
    Example 1:
    Input: 100
    Output: 933262154439441526816992388562667004-
         907159682643816214685929638952175999-
         932299156089414639761565182862536979-
         208272237582511852109168640000000000-
         00000000000000
    """
    number = 100

    assert (
        find_factorial(number)
        == 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
    )


def test_find_factorial_example_2():
    """
    Example 2:
    Input: 50
    Output: 3041409320171337804361260816606476884-
         4377641568960512000000000000
    """
    number = 50

    assert (
        find_factorial(number)
        == 30414093201713378043612608166064768844377641568960512000000000000
    )
