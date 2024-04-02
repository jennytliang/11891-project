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
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: open _ bra ckets
	"""
    # c = count of opening brackets
    # n = number of opening brackets
    # t = number of closing brackets

    c = 0
    n = 0
    t = 0

    for i in range(len(brackets)):
        if brackets[i] == '(':
            c += 1
            n += 1
        elif brackets[i] == ')':
            t += 1
        else:
            return False
    return c == n and t == n


if __name__ == '__main__':
    import doctest
    doctest.testmod()
