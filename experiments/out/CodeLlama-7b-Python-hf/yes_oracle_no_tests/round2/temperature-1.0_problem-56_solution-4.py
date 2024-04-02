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
    pass

def correct_bracketing_sol(brackets: str):
    # c: count
    nt = 0
    for b in brackets:
        if nt == 0 and b == '>':
            return False
        elif b == '<':
            nt += 1
        else:
            nt -= 1
    return True if nt == 0 else False

