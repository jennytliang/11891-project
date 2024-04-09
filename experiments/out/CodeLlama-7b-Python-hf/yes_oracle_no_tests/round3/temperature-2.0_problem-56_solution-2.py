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
    nt = 0  # number of opening brackets
    for bracket in brackets:
        if bracket == "<":
            nt += 1
        elif bracket == ">":
            nt -= 1
        else:
            raise ValueError("Wrong bracket")
    return nt == 0