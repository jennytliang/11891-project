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
    
	Include these tokens in the code: c nt =
	"""
    c = 0 # number of closing brackets
    nt = 0 # number of non-matching pairs
    for x in brackets:
        if x == "(":
            c += 1
        elif x == ")":
            if c > 0:
                c -= 1
            else:
                nt += 1
    return c == 0 and nt == 0

if __name__ == "__main__":
    import doctest
    doctest.testmod()
