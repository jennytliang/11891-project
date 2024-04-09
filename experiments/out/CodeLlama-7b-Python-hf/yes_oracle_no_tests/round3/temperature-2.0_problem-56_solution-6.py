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
    # c = 0
    # nt = 0
    c = 0
    nt = 0
    for i in brackets:
        if i == "<":
            c += 1
        if i == ">":
            nt += 1
    if c == nt:
        return True
    return False


def count_brackets(brackets: str):
    """ brackets is a string of "<" and ">".
    return the number of matching brackets.

    >>> count_brackets("<>")
    2
    >>> count_brackets("<<><>>")
    4
    >>> count_brackets("><<>")
    0
    """
    # c = 0
    # nt = 0
    c = 0
    nt = 0
    for i in brackets:
        if i == "<":
            c += 1
        if i == ">":
            nt += 1
    if c > nt:
        return nt
    else:
        return c


def correct_bracketing_complex(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing_complex("<")
    False
    >>> correct_bracketing_complex("<>")
    True
    >>> correct_bracketing_complex("<<><>>")
    True
    >>> correct_bracketing_complex("><<>")
    False
    """
    # c = 0
    # nt = 0
    c = 0
    nt = 0
    for i in brackets:
        if i == "<":
            c += 1
        if i == ">":
            nt += 1
    if c == nt:
        return True
    return False


def count_brackets_complex(brackets: str):
    """ brackets is a string of "<" and ">".
    return the number of matching brackets.

    >>> count_brackets_complex("<>")
    2
    >>> count