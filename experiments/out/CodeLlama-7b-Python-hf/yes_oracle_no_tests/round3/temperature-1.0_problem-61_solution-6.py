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
	Do not include these tokens in the code: opening _ bra ckets
	"""
    opening_brackets = 0
    closing_brackets = 0
    for i in brackets:
        if i == "(":
            opening_brackets += 1
        elif i == ")":
            closing_brackets += 1
    return opening_brackets == closing_brackets


if __name__ == "__main__":
    import doctest

    doctest.testmod()
