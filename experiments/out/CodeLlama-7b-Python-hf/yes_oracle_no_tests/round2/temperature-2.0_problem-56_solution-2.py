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
    
	Do not include these tokens in the code: #
	"""
    stack = []
    for bracket in brackets:
        if bracket == "<":
            stack.append(bracket)
        elif bracket == ">" and len(stack) > 0:
            stack.pop()
        else:
            return False
    return len(stack) == 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
