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
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: n t
	"""

    # c is the number of opening brackets, n is the number of closing brackets
    c, n = 0, 0

    for b in brackets:
        if b == "<":
            c += 1
        elif b == ">":
            n += 1
    
    return c == n


def correct_bracketing2(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing2("<")
    False
    >>> correct_bracketing2("<>")
    True
    >>> correct_bracketing2("<<><>>")
    True
    >>> correct_bracketing2("><<>")
    False
    
	Include these tokens in the code: c n t
	Do not include these tokens in the code: n t
	"""

    # c is the number of opening brackets, n is the number of closing brackets
    c, n = 0, 0

    for b in brackets:
        if b == "<":
            c += 1
        elif b == ">":
            n += 1
        else:
            # b is not "<" or ">"
            pass
    
    return c == n


if __name__ == "__main__":
    import doctest
    doctest.testmod()