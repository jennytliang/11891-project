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
    nt = 0 # count of '(' tokens
    for b in brackets:
        if b == '<':
            nt += 1
        elif b == '>' and nt > 0:
            nt -= 1
        elif b == '>' and nt == 0:
            return 0
    return nt == 0