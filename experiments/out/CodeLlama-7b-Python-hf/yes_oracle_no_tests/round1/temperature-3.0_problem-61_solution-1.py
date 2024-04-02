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
	Do not include these tokens in the code: open _ bra ckets
	"""

    #c nt = 0
    #open _ bra ckets = 0
    cnt = 0
    open_brackets = 0
    for i in brackets:
        if i == '(':
            cnt += 1
        elif i == ')':
            if cnt > 0:
                cnt -= 1
            else:
                return False
    if cnt == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
