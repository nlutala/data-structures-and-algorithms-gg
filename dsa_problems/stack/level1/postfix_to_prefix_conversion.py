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
    # Step 1. Postfix to infix
    operators = {"+", "-", "/", "*"}
    number_stack = []
    operator_stack = []
    infix = []

    for p in postfix_exp:
        if p not in operators:
            number_stack.append(p)
        else:
            operator_stack.append(p)

            if len(number_stack) != 0:
                infix.append(
                    "".join([number_stack[-2], operator_stack[-1], number_stack[-1]])
                )

                number_stack.pop()
                number_stack.pop()
                number_stack.append(infix[-1])
                infix = infix[1:]

    infix_exp = number_stack[0]

    # TODO: Implement Step 2. Infix to prefix
    number_stack.clear()
    operator_stack.clear()
    prefix = []

    return infix_exp
