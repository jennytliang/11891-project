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
	Do not include these tokens in the code: n t
	"""
    c = 0
    for i in brackets:
        if i == '(':
            c += 1
        if i == ')':
            c -= 1
        if c < 0:
            return False
    if c == 0:
        return True
    return False


def correct_bracketing2(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing2("(")
    False
    >>> correct_bracketing2("()")
    True
    >>> correct_bracketing2("(()())")
    True
    >>> correct_bracketing2(")(()")
    False
    
    Include these tokens in the code: c n t
    Do not include these tokens in the code: n t
    """
    c = 0
    for i in brackets:
        if i == '(':
            c += 1
        if i == ')':
            c -= 1
        if c < 0:
            return False
    if c == 0:
        return True
    return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()
