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
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: opening _ bra ckets =
	"""
    n_opening = 0
    for c in brackets:
        if c == '<':
            n_opening += 1
        elif c == '>':
            n_opening -= 1
        else:
            return False
    return n_opening == 0

















































































































































































































































































































































































































































