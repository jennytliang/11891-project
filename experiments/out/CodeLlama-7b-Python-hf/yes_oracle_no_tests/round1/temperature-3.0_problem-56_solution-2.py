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
    # c = number of opening brackets
    # n = number of closing brackets
    # t = number of opening brackets - number of closing brackets
    c = 0
    n = 0
    t = 0
    for i in brackets:
        if i == "<":
            c += 1
        if i == ">":
            n += 1
        if c < n:
            return False
    return True


print(correct_bracketing("<"))
print(correct_bracketing("<>"))
print(correct_bracketing("<<><>>"))
print(correct_bracketing("><<>"))
