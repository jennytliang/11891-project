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
    # TODO: implement this function
    # nt = 0
    # for c in brackets:
    #     if c == "<":
    #         nt += 1
    #     elif c == ">":
    #         nt -= 1
    # return nt == 0

    stack = []
    for i, b in enumerate(brackets):
        if b == '<':
            stack.append(i)
        elif b == '>':
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0


if __name__ == "__main__":
    import doctest
    doctest.testmod()
