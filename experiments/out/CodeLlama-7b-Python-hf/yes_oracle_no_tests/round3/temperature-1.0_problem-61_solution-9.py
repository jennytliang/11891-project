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
	Do not include these tokens in the code: n t
	"""

    # c -> count of opening brackets
    # nt -> not-closed list
    # t -> closed list
    # n -> nested list
    c, nt, t, n = 0, [], [], []

    for b in brackets:
        if b == "(":
            c += 1
            nt.append(b)
        elif b == ")":
            if nt == []:
                t.append(b)
            else:
                nt.pop()

    if c > 0:
        return False
    else:
        return True


print(correct_bracketing("(()())"))
print(correct_bracketing(")(()"))
print(correct_bracketing("(())()"))
print(correct_bracketing("((())())"))
print(correct_bracketing("((())"))
print(correct_bracketing("(()"))
print(correct_bracketing("(())"))
print(correct_bracketing("()()"))
print(correct_bracketing("()"))
print(correct_bracketing("(())()()"))
print(correct_bracketing("()()()"))
print(correct_bracketing("(()()()"))
print(correct_bracketing("((()()()()"))
print(correct_bracketing("()()()()"))
print(correct_bracketing("(((((((()))))))"))
print(correct_bracketing("((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((