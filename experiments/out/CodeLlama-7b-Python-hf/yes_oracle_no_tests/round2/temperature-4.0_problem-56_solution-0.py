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
    # c = count, n = not
    c = 0
    for char in brackets:
        if char == '<':
            c += 1
        elif char == '>':
            c -= 1
        if c < 0:
            return False
    return c == 0


if __name__ == "__main__":
    import doctest
    doctest.testmod()
