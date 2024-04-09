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
    c = 0 # c is the number of open brackets
    for i in brackets:
        if i == '(':
            c += 1
        elif i == ')':
            if c == 0:
                return False
            else:
                c -= 1
    return c == 0

print(correct_bracketing("("))
print(correct_bracketing("()"))
print(correct_bracketing("(()())"))
print(correct_bracketing(")(()"))