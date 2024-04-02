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

    opening_brackets = 0
    closing_brackets = 0

    for bracket in brackets:
        if bracket == "(":
            opening_brackets += 1
        elif bracket == ")":
            closing_brackets += 1

    return opening_brackets == closing_brackets


if __name__ == "__main__":
    import doctest

    doctest.testmod()
