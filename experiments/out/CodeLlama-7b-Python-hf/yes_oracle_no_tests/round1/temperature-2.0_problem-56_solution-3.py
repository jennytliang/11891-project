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
    # c is the number of opening brackets
    # n is the number of closing brackets
    # t is the number of opening and closing brackets
    c = 0
    n = 0
    t = 0
    for i in brackets:
        if i == "<":
            c += 1
        if i == ">":
            n += 1
        if i == "<" or i == ">":
            t += 1
    if c == t and n == t:
        return True
    else:
        return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
