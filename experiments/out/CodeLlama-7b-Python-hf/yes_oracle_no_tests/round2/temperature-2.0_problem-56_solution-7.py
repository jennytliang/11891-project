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

    opening = 0
    closing = 0

    for i in brackets:
        if i == "<":
            opening += 1
        elif i == ">":
            closing += 1

    if opening == closing:
        return True
    else:
        return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
