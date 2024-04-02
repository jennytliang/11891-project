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

    # TODO: implement this function!

    # raise NotImplementedError()

    nt = 0
    for c in brackets:
        if c == '<':
            nt += 1
        elif c == '>':
            nt -= 1

    return nt == 0


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
    
	Include these tokens in the code: c nt =
	"""

    # TODO: implement this function!

    # raise NotImplementedError()

    nt = []
    for c in brackets:
        if c == '<':
            nt.append('<')
        elif c == '>':
            if len(nt) == 0:
                return False
            else:
                nt.pop()
    return len(nt) == 0


def correct_bracketing_stack_optimized(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing_stack_optimized("<")
    False
    >>> correct_bracketing_stack_optimized("<>")
    True
    >>> correct_bracketing_stack_optimized("<<><>>")
    True
    >>> correct_bracketing_stack_optimized("><<>")
    False
    
	Include these tokens in the code: c nt =
	"""

    # TODO: implement this function!

    # raise NotImplementedError()

    nt = []
    for c in brackets:
        if c == '<':
            nt.append('<')