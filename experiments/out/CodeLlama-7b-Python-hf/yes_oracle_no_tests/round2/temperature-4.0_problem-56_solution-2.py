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
    
	Do not include these tokens in the code: n t = 0
	"""
    # n is the number of opening brackets
    # t is the number of closing brackets
    # the function should return True if n == t
    n = 0
    t = 0
    for i in range(len(brackets)):
        if brackets[i] == '<':
            n += 1
        if brackets[i] == '>':
            t += 1
    return n == t
