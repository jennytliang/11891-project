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
    # Write your code here.
    stack = []
    for b in brackets:
        if b == '<':
            stack.append(b)
        if b == '>':
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0


if __name__ == '__main__':
    import doctest
    doctest.testmod()
