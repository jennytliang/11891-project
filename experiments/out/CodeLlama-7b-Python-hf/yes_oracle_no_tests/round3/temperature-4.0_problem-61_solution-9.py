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
	Do not include these tokens in the code: # init n t
	"""
    # nt = number of closing brackets
    # ct = number of closing brackets
    # init = number of opening brackets
    init = 0
    nt = 0
    ct = 0
    for i in brackets:
        if i == "(":
            init += 1
        if i == ")":
            nt += 1
    ct = init - nt
    if ct == 0:
        return True
    else:
        return False


print(correct_bracketing("(()())"))
