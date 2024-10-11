"""
A file tests the height_of_tree function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.heaps.level1.height_of_heap_or_binary_tree import height_of_tree


def test_height_of_tree_example_1():
    """
    Example 1:
    Input : N = 6
    Output : 2
        ()
      /    \
     ()     ()
    /  \    /
  ()    () ()
    """
    n = 6
    assert height_of_tree(n) == 2


def test_height_of_tree_example_2():
    """
    Example 2:
    Input : N = 9
    Output : 3
        ()
      /    \
     ()     ()
    /  \    /  \
  ()    () ()   ()
 / \
()  ()
    """
    n = 9
    assert height_of_tree(n) == 3


# Custom tests just to be sure
def test_height_of_tree_example_3():
    """
    def test_height_of_tree_example_2():
    Example 3:
    Input: N = 11
    Output: 3
         ()
      /      \
     ()      ()
    /  \     /  \
  ()    ()  ()   ()
 / \   / \
()  () () ()
    """
    n = 11
    assert height_of_tree(n) == 3


def test_height_of_tree_example_4():
    """
    def test_height_of_tree_example_2():
    Example 4:
    Input: N = 2
    Output: 1
        ()
      /    \
     ()     ()
    """
    n = 2
    assert height_of_tree(n) == 1
