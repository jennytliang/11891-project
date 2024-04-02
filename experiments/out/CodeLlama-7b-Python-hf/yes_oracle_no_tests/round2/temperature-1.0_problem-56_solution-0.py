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
    to_eval = ""
    for c in brackets:
        if c == "<":
            to_eval += "("
        elif c == ">":
            to_eval += ")"
    return eval(to_eval)

if __name__ == '__main__':
    import doctest
    doctest.testmod()