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
    # c is the number of opening brackets
    # n is the number of closing brackets
    # t is the number of closing brackets that have not been matched with an opening bracket
    c, n, t = 0, 0, 0
    for b in brackets:
        if b == '(':
            c += 1
        elif b == ')':
            n += 1
            if c > 0:
                c -= 1
            else:
                t += 1
    return c == 0 and n == t


if __name__ == "__main__":
    import doctest
    doctest.testmod()
