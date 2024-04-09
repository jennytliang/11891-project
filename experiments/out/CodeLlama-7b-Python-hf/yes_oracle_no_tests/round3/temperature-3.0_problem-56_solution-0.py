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
    
	Do not include these tokens in the code: c nt = 0
	"""

    # c is the number of open brackets.
    # n is the number of closed brackets.
    # t is the number of tokens.
    c, n, t = 0, 0, 0
    for i in brackets:
        if i == "<": c += 1
        if i == ">": n += 1
        t += 1
    if c == n and t % 2 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()