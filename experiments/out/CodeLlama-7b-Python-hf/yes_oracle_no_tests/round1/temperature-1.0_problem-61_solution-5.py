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
    # c == 0, nt == 0
    # c == 0, nt == 1
    # c == 1, nt == 0
    # c == 1, nt == 1
    c = 0
    nt = 0
    for b in brackets:
        if b == '(':
            c += 1
        else:
            nt += 1
        if c < nt:
            return False
    return c == nt


print(correct_bracketing("()"))
print(correct_bracketing("()()()"))
print(correct_bracketing("((()))"))
print(correct_bracketing("((()))"))
print(correct_bracketing("((()))"))
print(correct_bracketing("((()))"))
print(correct_bracketing("((()))"))
print(correct_bracketing("((()))"))
print(correct_bracketing("((()))"))
print(correct_bracketing("((()))"))
print(correct_bracketing("((()))"))
print(correct_bracketing("((()))"))
print(correct_bracketing("((()))"))
print(correct_bracketing("((()))"))
print(correct_bracketing("((()))"))
print(correct_bracketing("((()))"))
print(correct_bracketing("((()))"))
print(correct_bracketing("((()))"))
print(correct_bracketing("((()))"))
print(correct_bracketing("((()))"))
print(correct_bracketing("((()))"))
print(correct_bracketing("((()))"))
print(correct_bracketing("((()))"))
print(correct_bracketing("((()))"))
print(correct_bracketing("((()))"))
print(correct_bracketing("((()))"))
print(correct_bracketing("((()))"))
print(correct_bracketing("((()))"))
print(correct_bracketing("((()))"))
print(correct_bracketing("((()))"))
print(correct_bracketing("((()))"))
print(correct_bracketing("((()))