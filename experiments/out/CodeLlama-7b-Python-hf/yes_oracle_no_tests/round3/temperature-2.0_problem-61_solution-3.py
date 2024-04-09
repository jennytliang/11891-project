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
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: n t
	"""
    # TODO: write some code
    stack = []
    for b in brackets:
        if b == "(":
            stack.append(b)
        elif b == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0


def correct_bracketing_stack(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing_stack("(")
    False
    >>> correct_bracketing_stack("()")
    True
    >>> correct_bracketing_stack("(()())")
    True
    >>> correct_bracketing_stack(")(()")
    False
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: n t
	"""
    # TODO: write some code
    stack = []
    for b in brackets:
        if b == "(":
            stack.append(b)
        elif b == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
