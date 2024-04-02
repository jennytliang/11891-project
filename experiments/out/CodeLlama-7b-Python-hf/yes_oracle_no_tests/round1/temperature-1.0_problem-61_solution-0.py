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
    stack = []
    for b in brackets:
        if b == '(':
            stack.append('(')
        else:
            if len(stack) < 1:
                return False
            else:
                stack.pop()
    
    if len(stack) > 0:
        return False
    else:
        return True