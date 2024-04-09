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
    # c is the current number of open brackets
    # n is the total number of brackets
    c, n = 0, len(brackets)
    for b in brackets:
        if b == '(':
            c += 1
        elif b == ')':
            c -= 1
        if c < 0:
            return False
    return c == 0


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
    # c is the current number of open brackets
    # n is the total number of brackets
    c, n = 0, len(brackets)
    for b in brackets:
        if b == '(':
            c += 1
        elif b == ')':
            c -= 1
        if c < 0:
            return False
    return c == 0

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
    # c is the current number of open brackets
    # n is the total number of brackets
    c, n = 0, len(brackets)
    for b in brackets:
        if b == '(':
            c += 1
        elif b == ')':
            c -= 1
        if c < 0:
            return False
