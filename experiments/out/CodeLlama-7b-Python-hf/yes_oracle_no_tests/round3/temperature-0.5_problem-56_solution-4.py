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
    #TODO: your code here
    stack = []
    for i in brackets:
        if i == '<':
            stack.append('<')
        elif i == '>':
            if stack == []:
                return False
            stack.pop()
    if stack == []:
        return True
    else:
        return False






if __name__ == '__main__':
    import doctest
    doctest.testmod()