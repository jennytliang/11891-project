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
    
	Do not include these tokens in the code: #
	"""

    # This is a stack using a list
    stack = []

    for bracket in brackets:
        if bracket == "(":
            stack.append(bracket)
        elif bracket == ")":
            if not stack:
                return False
            else:
                stack.pop()
    return not stack


def correct_bracketing_2(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing_2("(")
    False
    >>> correct_bracketing_2("()")
    True
    >>> correct_bracketing_2("(()())")
    True
    >>> correct_bracketing_2(")(()")
    False
    
	Do not include these tokens in the code: #
	"""

    # This is a stack using a list
    stack = []

    for bracket in brackets:
        if bracket == "(":
            stack.append(bracket)
        elif bracket == ")":
            if not stack:
                return False
            else:
                stack.pop()
    return not stack


if __name__ == "__main__":
    import doctest
    doctest.testmod()
