"""
A file tests the format_key function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.string.level2.license_key_formatting import format_key


def test_format_key_example_1():
    """
    Example 1:
    Input: S = “5F3Z-2e-9-w”, K = 4
    Output: “5F3Z-2E9W”
    Explanation: The string S has been split into two parts,  
    each part has 4 characters. 
    Note that two extra dashes are not needed and can be removed.
    """
    s, k = "5F3Z-2e-9-w", 4
    assert format_key(s, k) == "5F3Z-2E9W"


def test_format_key_example_2():
    """
    Example 2:
    Input: S = “2-5g-3-J”, K = 2
    Output: “2-5G-3J”
    Explanation: The string s has been split into three parts,  
    each part has 2 characters except the first part 
    as it could be shorter as mentioned above
    """
    s, k = "2-5g-3-J", 2
    assert format_key(s, k) == "2-5G-3J"


# Custom tests (not convinced my solution works 100%)
def test_format_key_example_3():
    """
    Example 3:
    Input: S = “2-5g-3-J-XVYZ-sh”, K = 3
    Output: “25-G3J-XVY-ZSH”
    """
    s, k = "2-5g-3-J-XVYZ-sh", 3
    assert format_key(s, k) == "25-G3J-XVY-ZSH"


def test_format_key_example_4():
    """
    Example 4:
    Input: S = “2-5g-3-J-XVYZ-sh”, K = 4
    Output: “25G-3JXV-YZSH”
    """
    s, k = "2-5g-3-J-XVYZ-sh", 4
    assert format_key(s, k) == "25G-3JXV-YZSH"
