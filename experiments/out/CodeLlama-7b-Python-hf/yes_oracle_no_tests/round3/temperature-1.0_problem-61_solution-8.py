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
	Do not include these tokens in the code: # count the number of opening brackets
	"""
    # c is the number of opening brackets
    # n is the number of closing brackets
    # t is the number of matching brackets
    c = 0
    n = 0
    t = 0
    for i in brackets:
        if i == "(":
            c += 1
        elif i == ")":
            n += 1
            if c == n:
                t += 1
            else:
                return False
        else:
            return False
    if c == n == t:
        return True
    else:
        return False


print(correct_bracketing("(()())"))
print(correct_bracketing(")(()"))
print(correct_bracketing("("))
print(correct_bracketing("()"))
print(correct_bracketing("(()()"))
print(correct_bracketing("(()())"))
print(correct_bracketing("(()()"))

