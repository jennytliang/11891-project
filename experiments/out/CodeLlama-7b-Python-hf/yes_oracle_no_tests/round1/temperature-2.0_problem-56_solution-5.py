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
    
	Include these tokens in the code: c nt =
	"""
    nt = 0
    for i in range(len(brackets)):
        if brackets[i] == "<":
            nt += 1
        elif brackets[i] == ">":
            nt -= 1
        if nt < 0:
            return False
    if nt == 0:
        return True
    return False


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
    
	Include these tokens in the code: c nt =
	"""
    nt = 0
    for i in range(len(brackets)):
        if brackets[i] == "<":
            nt += 1
        elif brackets[i] == ">":
            nt -= 1
        if nt < 0:
            return False
    if nt == 0:
        return True
    return False


# print(correct_bracketing(input("Enter brackets: ")))
