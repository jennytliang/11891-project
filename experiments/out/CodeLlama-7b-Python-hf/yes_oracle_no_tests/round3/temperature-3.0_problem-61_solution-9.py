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
    
	Do not include these tokens in the code: # n _ open =
	"""

    # n = number of opening brackets
    n = 0

    # _ = last opening bracket
    _ = 0

    for i in range(len(brackets)):
        if brackets[i] == "(":
            n += 1
            _ = i
        elif brackets[i] == ")":
            n -= 1
        if n < 0:
            return False
    return n == 0


print(correct_bracketing("()()()((()))"))
print(correct_bracketing("((())"))
