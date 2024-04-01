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
	Do not include these tokens in the code: stack
	"""

    s = []
    for c in brackets:
        if c == '<':
            s.append(c)
        elif c == '>':
            if s == []:
                return False
            else:
                s.pop()
    return s == []


def correct_bracketing_stack(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing_stack("<")
    False
    >>> correct_bracketing_stack("<>")
    True
    >>> correct_bracketing_stack("<<><>>")
    True
    >>> correct_bracketing_stack("><<>")
    False
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: stack
	"""

    s = []
    for c in brackets:
        if c == '<':
            s.append(c)
        elif c == '>':
            if s == []:
                return False
            else:
                s.pop()
    return s == []


if __name__ == "__main__":
    import doctest
    doctest.testmod()
