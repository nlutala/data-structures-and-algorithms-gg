"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/

Author: Nathan Lutala (nlutala)
"""


def parenthesis_checker(exp: str) -> str:
    """
    Given an expression string exp, write a program to examine whether the pairs and the
    orders of “{“, “}”, “(“, “)”, “[“, “]” are correct in the given expression.\n

    :param - exp (the string expression)
    """
    list_exp = list(exp)
    stack = []
    parenthesis_dict = {
        "[": "]", "{": "}", "(": ")"
    }

    for p in list_exp:
        if stack != []:
            if p == parenthesis_dict.get(stack[-1]):
                stack.pop()
        else:
            stack.append(p)

    if stack == []:
        return "Balanced"
    else:
        return "Not Balanced"


if __name__ == "__main__":

    def test_parenthesis_checker_example_1():
        """
        Example 1:
        Input: exp = “[()]{}{[()()]()}”
        Output: Balanced
        Explanation: all the brackets are well-formed
        """
        exp = "[()]{}{[()()]()}"
        return parenthesis_checker(exp) == "Balanced"


    def test_parenthesis_checker_example_2():
        """
        Example 2:
        Input: exp = “[(])”
        Output: Not Balanced
        Explanation: 1 and 4 brackets are not balanced because
        there is a closing ‘]’ before the closing ‘(‘
        """
        exp = "[(])"
        return parenthesis_checker(exp) == "Not Balanced"

    print(
        test_parenthesis_checker_example_1(),
        test_parenthesis_checker_example_2(),
    )
