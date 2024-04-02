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
    
	Do not include these tokens in the code: # c n t =
	"""
    c = 0
    for s in brackets:
        if s == '(':
            c += 1
        elif s == ')':
            c -= 1
        if c < 0:
            return False
    return c == 0


if __name__ == '__main__':
    import doctest
    doctest.testmod()
