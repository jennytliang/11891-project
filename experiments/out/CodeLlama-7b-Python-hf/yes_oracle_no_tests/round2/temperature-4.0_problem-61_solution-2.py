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
	Do not include these tokens in the code: counter
	"""
    c = 0
    for nt in brackets:
        if nt == '(':
            c += 1
        elif nt == ')':
            if c == 0:
                return False
            else:
                c -= 1
    return c == 0


print(correct_bracketing("("))
print(correct_bracketing("()"))
print(correct_bracketing("(()())"))
print(correct_bracketing(")(()"))
