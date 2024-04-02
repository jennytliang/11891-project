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
    
	Include these tokens in the code: c nt =
	"""
    # count the number of opening brackets
    # count the number of closing brackets
    # return True if the number of opening brackets is equal to the number of closing brackets
    c = 0
    nt = 0
    for b in brackets:
        if b == '(':
            c += 1
        if b == ')':
            nt += 1
    return c == nt


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
    """
    stack = []
    for b in brackets:
        if b == '(':
            stack.append(b)
        if b == ')':
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0


if __name__ == '__main__':
    import doctest
    doctest.testmod()
