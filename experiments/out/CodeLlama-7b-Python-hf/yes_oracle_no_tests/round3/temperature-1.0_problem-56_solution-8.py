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
	Do not include these tokens in the code: count
	"""
    # c: count of open brackets, n: count of close brackets
    c, n = 0, 0
    for b in brackets:
        if b == "<":
            c += 1
        else:
            n += 1
        if c < n:
            return False
    return c == n


if __name__ == "__main__":
    import doctest
    doctest.testmod()
