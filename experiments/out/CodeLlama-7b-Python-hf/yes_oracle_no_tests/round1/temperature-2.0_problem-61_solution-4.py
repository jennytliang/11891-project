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
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: opening
	"""
    c = 0
    nt = 0
    for i in brackets:
        if i == "(":
            c += 1
        if i == ")":
            nt += 1
    return c == nt


print(correct_bracketing("(()())"))