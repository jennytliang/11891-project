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

    # TODO: implement this
    stack = []
    for c in brackets:
        if c == '<':
            stack.append(c)
        elif c == '>':
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0


def correct_bracketing_2(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing_2("<")
    False
    >>> correct_bracketing_2("<>")
    True
    >>> correct_bracketing_2("<<><>>")
    True
    >>> correct_bracketing_2("><<>")
    False
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: n t
	"""

    # TODO: implement this
    stack = []
    for c in brackets:
        if c == '<':
            stack.append(c)
        elif c == '>':
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0


if __name__ == "__main__":
    import doctest
    doctest.testmod()
