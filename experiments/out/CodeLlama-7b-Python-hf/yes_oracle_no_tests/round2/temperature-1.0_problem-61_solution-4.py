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
    nt = len(brackets)
    c = 0 # counter for no of opening brackets
    for i in range(0, nt, 1):
        if brackets[i] == '(':
            c += 1
        elif brackets[i] == ')':
            c -= 1
        if c < 0:
            return False
    if c != 0:
        return False
    return True
    

print(F"correct_bracketing.py: correct_bracketing('(()())') = True = {correct_bracketing('(()())')}")
print(F"correct_bracketing.py: correct_bracketing(')(') = False = {correct_bracketing(')(')}")
