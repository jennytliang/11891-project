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
    cnt = 0
    for b in brackets:
        if b == "<":
            cnt += 1
        elif b == ">":
            cnt -= 1
        if cnt < 0:
            return False
    return cnt == 0


def correct_bracketing_stack(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing_stack("<")
    False
    >>> correct_bracketing_stack("<>")
    True
    >>> correct_bracketing_stack("<<><>>")
    True
    >>> correct_bracketing_stack("><<>")
    False
    
	Include these tokens in the code: c nt =
	"""
    stack = []
    for b in brackets:
        if b == "<":
            stack.append("<")
        elif b == ">":
            if stack.pop() != "<":
                return False
    return len(stack) == 0


if __name__ == "__main__":
    import doctest
    doctest.testmod()
