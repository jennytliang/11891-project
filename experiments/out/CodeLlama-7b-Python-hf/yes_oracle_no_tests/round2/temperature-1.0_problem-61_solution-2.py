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
    
	Include these tokens in the code: c nt =
	"""
    stack = []
    nt = [ch for ch in brackets if ch in '()']                     # nt = notations used as tokens
    c = 0                                                          # loop variable
    for elem in nt:                                                # scan each elem of brackets
        if elem[c] == '(':
            stack.append('(')                                                        # if current elem is (
            # print "Stack has become ", stack
        elif elem[c] == ')':
            if len(stack) == 0:                                           # and there is nothing in the stack (empty)
                return False                                        # (is not present in the stack)
            if elem[c] != stack.pop():
                return False            # then current elem] is ) is not equal to last elem of the stack
            # print "Stack has ", stack
    return True
    
    

  
#correct_bracketing("()))")   prints true

# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()



# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()

