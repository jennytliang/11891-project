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
	Do not include these tokens in the code: n _ open
	"""
    
    # n _ open = number of opening brackets
    # c = number of closing brackets
    # return True if c == n _ open
    n_open = 0
    c = 0
    for b in brackets:
        if b == '(':
            n_open += 1
        elif b == ')':
            c += 1
            if c > n_open:
                return False
    return c == n_open

print(correct_bracketing("(()())"))
print(correct_bracketing(")("))
print(correct_bracketing("()()(()"))
print(correct_bracketing("()()()"))
print(correct_bracketing("(()()"))
print(correct_bracketing("()()()()"))
print(correct_bracketing(")(()"))
print(correct_bracketing("()()()()()"))
print(correct_bracketing("()()()()()()"))
print(correct_bracketing("(()()()"))
print(correct_bracketing("(()()()()"))
print(correct_bracketing("(()()()()()"))
print(correct_bracketing("(()()()()()()"))
print(correct_bracketing("(()()()()()()()"))
print(correct_bracketing("(()()()()()()()()"))
print(correct_bracketing("(()()()()()()()()()"))
print(correct_bracketing("(()()()()()()()()()()"))
print(correct_bracketing("(()()()()()()()()()()()"))
print(correct_bracketing("(()()()()()()()()()()()()"))
print(correct_bracketing("(()()()()()()()()()()()()()"))
print(correct_bracketing("(()()()()()()()()()()()()()()"))
print(correct_bracketing("(()()()()()()()()()()()()()()()"))
print(correct_bracketing("(()()()()()()()()()()()()()()()()"))
print(correct