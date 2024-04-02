def correct_bracketing(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: n = len ( bra
	"""
    
    if len(brackets) % 2 != 0:
        return False
    stack = []
    for i in range(len(brackets)):
        if brackets[i] == ">":
            if not stack:
                return False
            else:
                stack.pop()
        else:
            stack.append(">")
    return not stack


print(correct_bracketing("<<><>>"))
print(correct_bracketing("><<>"))
