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
    nt = 0 # number of open brackets
    for c in brackets:
        if c == '<':
            nt += 1
        elif c == '>':
            nt -= 1
        if nt < 0:
            return False
    return nt == 0


def test_correct_bracketing():
    assert correct_bracketing('<>') == True
    assert correct_bracketing('<><') == True
    assert correct_bracketing('<>') == True
    assert correct_bracketing('<<><>>') == True
    assert correct_bracketing('><<>') == False
    assert correct_bracketing('<') == False
    assert correct_bracketing('><') == False
    assert correct_bracketing('>') == False
    assert correct_bracketing('') == True
    assert correct_bracketing('<><<>') == False
    assert correct_bracketing('<<><>><') == False


if __name__ == '__main__':
    import doctest
    doctest.testmod()