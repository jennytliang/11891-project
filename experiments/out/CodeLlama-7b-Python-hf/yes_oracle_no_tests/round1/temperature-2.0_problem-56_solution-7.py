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

    # c = 0
    # nt = 0
    # for i in brackets:
    #     if i == "<":
    #         c += 1
    #     elif i == ">":
    #         nt += 1
    # if c == nt:
    #     return True
    # return False

    # c = 0
    # nt = 0
    # for i in brackets:
    #     if i == "<":
    #         c += 1
    #     elif i == ">":
    #         nt += 1
    # if c == nt:
    #     return True
    # return False

    c = 0
    nt = 0
    for i in brackets:
        if i == "<":
            c += 1
        elif i == ">":
            nt += 1
    if c == nt:
        return True
    return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
