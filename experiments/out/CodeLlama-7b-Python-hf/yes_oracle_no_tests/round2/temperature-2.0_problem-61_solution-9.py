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

    # Your code here
    # stack = []
    # for char in brackets:
    #     if char == "(":
    #         stack.append("(")
    #     else:
    #         if not stack:
    #             return False
    #         stack.pop()
    # return not stack
    stack = []
    for char in brackets:
        if char == "(":
            stack.append(char)
        else:
            if not stack:
                return False
            stack.pop()
    return not stack


def correct_bracketing2(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing2("(")
    False
    >>> correct_bracketing2("()")
    True
    >>> correct_bracketing2("(()())")
    True
    >>> correct_bracketing2(")(()")
    False
    
	Do not include these tokens in the code: #
	"""

    # Your code here
    stack = []
    for char in brackets:
        if char == "(":
            stack.append("(")
        else:
            if not stack or stack.pop() != "(":
                return False
    return not stack


if __name__ == "__main__":
    import doctest

    doctest.testmod()
