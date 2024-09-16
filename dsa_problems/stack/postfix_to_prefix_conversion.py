"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/postfix-prefix-conversion/

Author: Nathan Lutala (nlutala)
"""


def postfix_to_prefix(postfix_exp: str) -> str:
    """
    Given a Postfix expression, convert it into a Prefix expression.\n

    :param - postfix_exp (the postfix expression)\n

    Return the prefix expression string.
    """
    # Using the guide below (I didn't understand it):
    # Read the Postfix expression from left to right
    # If the symbol is an operand, then push it onto the Stack
    # If the symbol is an operator, then pop two operands from the Stack
    # Create a string by concatenating the two operands and the operator before them.
    # string = operator + operand2 + operand1
    # And push the resultant string back to Stack
    # Repeat the above steps until end of Postfix expression.
    stack = []
    operators = {"+", "-", "/", "*"}
    prefix_exp = ""

    for p in postfix_exp:
        if p not in operators:
            stack.append(p)
        else:
            if len(stack) == 1:
                prefix_exp = prefix_exp + stack.pop()
            elif len(stack) >= 2:
                prefix_exp = prefix_exp + stack.pop() + stack.pop()

    return prefix_exp


if __name__ == "__main__":

    def test_postfix_to_prefix_example_1():
        """
        Example 1:
        Input :  Postfix : AB+CD-*
        Output : Prefix :  *+AB-CD
        Explanation : Postfix to Infix : (A+B) * (C-D)
        Infix to Prefix :  *+AB-CD
        """
        exp = "AB+CD-*"
        return postfix_to_prefix(exp) == "*+AB-CD"


    def test_postfix_to_prefix_example_2():
        """
        Example 2:
        Input :  Postfix : ABC/-AK/L-*
        Output : Prefix :  *-A/BC-/AKL
        Explanation : Postfix to Infix : ((A-(B/C))*((A/K)-L))
        Infix to Prefix :  *-A/BC-/AKL
        """
        exp = "ABC/-AK/L-*"
        return postfix_to_prefix(exp) == "*-A/BC-/AKL"

    print(
        test_postfix_to_prefix_example_1(),
        test_postfix_to_prefix_example_2(),
    )
