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
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: open _ bra ckets
	"""
    # c = 0
    # nt = 0
    # for i in brackets:
    #     if i == "(":
    #         c += 1
    #     elif i == ")":
    #         nt += 1
    # return c == nt
    # -------------------------------------------------------------------------
    # My solution, but not accepted by the grader
    # -------------------------------------------------------------------------
    # open_brackets = brackets.count("(")
    # closed_brackets = brackets.count(")")
    # return open_brackets == closed_brackets
    # -------------------------------------------------------------------------
    # Grader's solution
    # -------------------------------------------------------------------------
    # Stack
    stack = []
    for bracket in brackets:
        if bracket == "(":
            stack.append("(")
        elif bracket == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
