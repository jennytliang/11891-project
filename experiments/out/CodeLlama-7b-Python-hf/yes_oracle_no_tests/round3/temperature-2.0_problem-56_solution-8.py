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
	Do not include these tokens in the code: n t
	"""
    # 0: c, 1: n, 2: t
    stack = []
    for i in brackets:
        if i == "<":
            stack.append("c")
        elif i == ">":
            if stack and stack[-1] == "c":
                stack.pop()
            else:
                return False
    return len(stack) == 0


def correct_bracketing2(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing2("<")
    False
    >>> correct_bracketing2("<>")
    True
    >>> correct_bracketing2("<<><>>")
    True
    >>> correct_bracketing2("><<>")
    False
    
	Include these tokens in the code: c n t
	Do not include these tokens in the code: n t
	"""
    # 0: c, 1: n, 2: t
    stack = []
    for i in brackets:
        if i == "<":
            stack.append("c")
        elif i == ">":
            if stack and stack[-1] == "c":
                stack.pop()
            else:
                return False
    return len(stack) == 0
