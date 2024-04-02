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
    # cnt = 0
    # nt = 0
    # for i in brackets:
    #     if i == "<":
    #         cnt += 1
    #     elif i == ">":
    #         nt += 1
    # if cnt == nt:
    #     return True
    # else:
    #     return False
    return brackets.count("<") == brackets.count(">")


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
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: n t
	"""
    if brackets == "":
        return True
    elif brackets[0] == "<":
        return correct_bracketing(brackets[1:])
    elif brackets[0] == ">":
        return correct_bracketing(brackets[1:])
    else:
        return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
