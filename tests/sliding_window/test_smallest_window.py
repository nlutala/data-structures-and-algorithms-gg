"""
A file tests the find_smallest_window function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.sliding_window.smallest_window import find_smallest_window


def test_find_smallest_window_example_1() -> None:
    """
    Example 1
    Input: S = “timetopractice”, P = “toc”
    Output: toprac
    Explanation: “toprac” is the smallest substring in which “toc” can be found.
    """
    s = "timetopractice"
    p = "toc"
    assert find_smallest_window(s, p) == "toprac"


def test_find_max_of_subarray_example_2() -> None:
    """
    Example 2
    Input: S = “zoomlazapzo”, P = “oza”
    Output: apzo
    Explanation: “apzo” is the smallest substring in which “oza” can be found.
    """
    s = "zoomlazapzo"
    p = "oza"
    assert find_smallest_window(s, p) == "apzo"
