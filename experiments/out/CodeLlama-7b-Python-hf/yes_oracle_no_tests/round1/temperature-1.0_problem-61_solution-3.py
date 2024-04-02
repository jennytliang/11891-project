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
    
	Include these tokens in the code: c nt =
	"""
    # Your code here
    nt = 0
    c = 0
    for i in brackets:
        if i == '(':
            c += 1
        else:
            c -= 1
        if c < 0:
            return False
    if c == 0:
        return True
    return False


print(correct_bracketing("(()())"))
