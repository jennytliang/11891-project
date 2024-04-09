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
    # c is the number of open brackets
    # n is the number of closing brackets
    c = 0
    n = 0
    for i in range(len(brackets)):
        if brackets[i] == "(":
            c += 1
        if brackets[i] == ")":
            n += 1
    return c == n


if __name__ == "__main__":
    import doctest

    doctest.testmod()
