"""
A file tests the is_valid_ip function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.string.level2.validate_an_ip_address import is_valid_ip


def test_is_valid_ip_example_1():
    """
    Example 1:
    Input: ip = "128.0.0.1"
    Output: "Valid"
    """
    ip = "128.0.0.1"
    assert is_valid_ip(ip) == "Valid"


def test_is_valid_ip_example_2():
    """
    Example 2:
    Input: ip = "125.16.100.1"
    Output: "Valid"
    """
    ip = "125.16.100.1"
    assert is_valid_ip(ip) == "Valid"


def test_is_valid_ip_example_3():
    """
    Example 3:
    Input: ip = "125.512.100.1"
    Output: "Not valid"
    """
    ip = "125.512.100.1"
    assert is_valid_ip(ip) == "Not valid"


def test_is_valid_ip_example_4():
    """
    Example 4:
    Input: ip = "125.512.100.abc"
    Output: "Not valid"
    """
    ip = "125.512.100.abc"
    assert is_valid_ip(ip) == "Not valid"
