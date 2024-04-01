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
	Do not include these tokens in the code: stack
	"""

    s = 0  # number of open brackets
    for c in brackets:
        if c == '(':
            s += 1
        elif c == ')':
            s -= 1

    return s == 0


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
	Do not include these tokens in the code: stack
	"""

    s = 0  # number of open brackets
    for c in brackets:
        if c == '(':
            s += 1
        elif c == ')':
            s -= 1
        else:
            raise ValueError("Unexpected token")

    return s == 0


if __name__ == '__main__':
    import doctest
    doctest.testmod()
