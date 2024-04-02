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
    nt = 0
    for c in brackets:
        if c == "<":
            nt += 1
        else:
            nt -= 1
        if nt < 0:
            return False
    return nt == 0


def correct_bracketing_v2(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing_v2("<")
    False
    >>> correct_bracketing_v2("<>")
    True
    >>> correct_bracketing_v2("<<><>>")
    True
    >>> correct_bracketing_v2("><<>")
    False
    """
    nt = 0
    for c in brackets:
        if c == "<":
            nt += 1
        elif c == ">":
            if nt == 0:
                return False
            else:
                nt -= 1
    return nt == 0


def correct_bracketing_v3(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing_v3("<")
    False
    >>> correct_bracketing_v3("<>")
    True
    >>> correct_bracketing_v3("<<><>>")
    True
    >>> correct_bracketing_v3("><<>")
    False
    """
    nt = 0
    for c in brackets:
        if c == "<":
            nt += 1
        elif c == ">":
            nt -= 1
        if nt < 0:
            return False
    return nt == 0


# print(correct_bracketing_v3('<<><>>'))
# print(correct_bracketing_v3('><<>'))
# print(correct_bracketing_v3('<><'))
# print(correct_bracketing_v3('><