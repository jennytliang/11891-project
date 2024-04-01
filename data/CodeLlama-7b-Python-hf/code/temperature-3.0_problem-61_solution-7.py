def correct_bracketing(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    """
    open_brackets = 0

    for c in brackets:
        if c == "(":
            open_brackets += 1
        elif c == ")":
            open_brackets -= 1
            if open_brackets < 0:
                return False
    return open_brackets == 0


def balancedParentheses(s):
    stack = []

    if s[0] == ")" or s[-1] == "(":
        return False

    for i in s:
        if i == ")":
            if len(stack) == 0:
                return False
            stack.pop()
        else:
            stack.append("(")

    return len(stack) == 0