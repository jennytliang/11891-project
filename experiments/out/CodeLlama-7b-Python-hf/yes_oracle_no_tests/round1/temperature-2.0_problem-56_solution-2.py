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
    # for b in brackets:
    #     if b == "<":
    #         c += 1
    #     elif b == ">":
    #         nt += 1
    # return c == nt
    # 
    # c = 0
    # nt = 0
    # for b in brackets:
    #     if b == "<":
    #         c += 1
    #     elif b == ">":
    #         nt += 1
    # return c == nt

    c = 0
    for b in brackets:
        if b == "<":
            c += 1
        elif b == ">":
            c -= 1
    return c == 0


if __name__ == "__main__":
    import doctest
    doctest.testmod()