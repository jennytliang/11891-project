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
    # cn = counting number of opening bracket
    
    cn = 0
    for i in brackets: 
        if i == ')':
            cn = cn-1 
        else:
            cn = cn+1 
        if cn<0:
            return False
        else:
            return True