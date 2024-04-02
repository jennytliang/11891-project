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
	Do not include these tokens in the code: counter
	"""
    c = 0
    for i in brackets:
        if i == '(':
            c += 1
        elif i == ')':
            c -= 1
        if c < 0:
            return False
    return c == 0


def correct_bracketing_2(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing_2("(")
    False
    >>> correct_bracketing_2("()")
    True
    >>> correct_bracketing_2("(()())")
    True
    >>> correct_bracketing_2(")(()")
    False
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: counter
	"""
    c = 0
    for i in brackets:
        if i == '(':
            c += 1
        elif i == ')':
            c -= 1
        if c < 0:
            return False
    return c == 0



