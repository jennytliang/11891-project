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

    n_open = 0
    for char in brackets:
        if char == ">":
            n_open -= 1
        else:
            n_open += 1
        if n_open < 0:
            return False
    return n_open == 0


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

    """
    stack = []
    for char in brackets:
        if char == ">":
            if stack and stack[-1] == "<":
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    return len(stack) == 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
