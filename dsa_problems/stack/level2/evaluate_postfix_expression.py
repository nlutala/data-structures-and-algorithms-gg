"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/evaluation-of-postfix-expression/

Author: Nathan Lutala (nlutala)
"""


def evaluate_postfix(expression: str) -> int:
    """
    Given a postfix expression, the task is to evaluate the postfix expression.\n

    Postfix expression: The expression of the form “a b operator” (ab+) i.e., when a
    pair of operands is followed by an operator.\n

    :param - expression (a string)\n

    Returns the result of the postfix expression.
    """
    operators = ["+", "-", "/", "*"]
    stack = []

    for token in expression.split(" "):
        if token not in operators:
            stack.append(token)
        else:
            num2, num1 = stack.pop(), stack.pop()
            stack.append(str(eval(num1 + token + num2)))

    # Annoying solution to get around the 757.0 for the second test
    return int(stack[0].split(".")[0])
