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
	Do not include these tokens in the code: counter
	"""
    
    counter = 0
    for c in brackets:
        if c == "(":
            counter += 1
        elif c == ")":
            counter -= 1
        if counter < 0:
            return False
    return counter == 0


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(correct_bracketing("(()())"))