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

    s = []
    for i in brackets:
        if i == '(':
            s.append('(')
        elif i == ')':
            if len(s) == 0:
                return False
            else:
                s.pop()
    if len(s) == 0:
        return True
    else:
        return False
