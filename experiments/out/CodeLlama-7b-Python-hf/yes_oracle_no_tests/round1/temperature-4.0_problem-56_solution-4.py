def correct_bracketing(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    
	Include these tokens in the code: c nt =
	"""
    # c = 0 #counter
    # nt = 0 #not matched
    # for i in brackets:
    #     if i == "<":
    #         c += 1
    #     if i == ">":
    #         c -= 1
    #     if c < 0:
    #         nt += 1
    # if nt == 0:
    #     return True
    # else:
    #     return False

    stack = []
    for i in brackets:
        if i == "<":
            stack.append(i)
        if i == ">":
            stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
