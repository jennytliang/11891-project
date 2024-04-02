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
    
	Include these tokens in the code: c nt =
	"""
    n_closed = 0
    n_open = 0
    for c in brackets:
        if not c == '<' and n_closed > n_open: 
            return False
        if c == '<': 
            n_open += 1
        else: n_closed += 1    
    return (n_closed == n_open)