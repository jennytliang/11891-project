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
    # base case
    if len(brackets) == 0:
        return True
    # recursive case
    if brackets[0] == '<':
        if brackets[len(brackets)-1] == '>':
            return correct_bracketing(brackets[1:len(brackets)-1])
        else:
            return False
    else:
        return correct_bracketing(brackets[1:])





if __name__ == "__main__":
    import doctest
    doctest.testmod()