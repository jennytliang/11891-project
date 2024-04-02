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
    
	Include these tokens in the code: nt
	"""

    # init nt
    nt = 0
    # loop through brackets
    for i in range(0,len(brackets)):
        # if there's an opening bracket
        if brackets[i] == '(':
            nt += 1
        # if there's a closing bracket
        elif brackets[i] == ')':
            nt -= 1
        # if there's a closing bracket but no opening bracket
        if nt < 0:
            return False
    # if there are an odd number of opening brackets
    if nt % 2 == 1:
        return False
    # if there are an even number of opening and closing brackets
    else:
        return True





def correct_bracketing2(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing2("(")
    False
    >>> correct_bracketing2("()")
    True
    >>> correct_bracketing2("(()())")
    True
    >>> correct_bracketing2(")(()")
    False
    
	Include these tokens in the code: nt
	"""

    # init nt
    nt = 0
    # loop through brackets
    for i in range(0,len(brackets)):
        # if there's an opening bracket
        if brackets[i] == '(':
            nt += 1
        # if there's a closing bracket
        elif brackets[i] == ')':
            nt -= 1
        # if there's a closing bracket but no opening bracket
        if nt < 0:
            return False
    # if there are an odd number of opening brackets
    if nt % 2 == 1:
        return False
    # if there are an even number of opening and closing brackets
    else:
        return True





def correct_bracketing3(brackets: str):
    """ brackets is a string of "(" and ")".
   