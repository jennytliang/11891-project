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
	Do not include these tokens in the code: opening
	"""
    # c is a counter that counts the number of opening brackets
    # nt is a counter that counts the number of closing brackets
    c, nt = 0, 0

    # loop over the brackets
    for bracket in brackets:
        # if the bracket is an opening bracket
        if bracket == '(':
            # increment c
            c += 1
            # if c is greater than 0
            if c > 0:
                # increment nt
                nt += 1
        # if the bracket is a closing bracket
        elif bracket == ')':
            # decrement c
            c -= 1
            # if nt is greater than 0
            if nt > 0:
                # increment nt
                nt += 1
        # if c is 0 and nt is greater than 0
        if c == 0 and nt > 0:
            # return False
            return False
    # if c is 0 and nt is 0
    if c == 0 and nt == 0:
        # return True
        return True
    # return False
    return False


print(F"correct_bracketing.py: correct_bracketing('(') = `False` = `{correct_bracketing('(')}`")
print(F"correct_bracketing.py: correct_bracketing('()') = `True` = `{correct_bracketing('()')}`")
print(F"correct_bracketing.py: correct_bracketing('(()())') = `True` = `{correct_bracketing('(()())')}`")
print(F"correct_bracketing.py: correct_bracketing(')(()') = `False` = `{correct_bracketing(')(()')}`")
