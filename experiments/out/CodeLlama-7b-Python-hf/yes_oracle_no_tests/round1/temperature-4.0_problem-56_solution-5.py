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

    # c is a counter of the number of open brackets
    c = 0
    # nt is a boolean that is true when there are no more open brackets
    nt = False
    # for each character in brackets
    for b in brackets:
        # if it is an open bracket, increment c by 1
        if b == "<":
            c += 1
        # if it is a close bracket, decrement c by 1
        if b == ">":
            c -= 1
        # if c is negative, return False
        if c < 0:
            return False
    # if c is not 0, return False
    if c != 0:
        return False
    # otherwise, return True
    return True


# print(correct_bracketing("<>"))
