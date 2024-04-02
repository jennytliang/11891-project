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
    nt= 0 #c= 0 is implicitely initialised, but I chose to be explicit for readability
    for i in brackets:
        if i == "(":
            nt += 1
        elif i == ")":
            nt -=1
        if nt < 0:
            return False
    return nt == 0
    

a = correct_bracketing("(()())")
print(a)
