def correct_bracketing(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    
	Include these tokens in the code: nt
	"""

    nt = 0
    for c in brackets:
        if c == "(":
            nt += 1
        elif c == ")":
            nt -= 1
        if nt < 0:
            return False
    return nt == 0


print(correct_bracketing("(()())"))
