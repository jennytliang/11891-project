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
	Do not include these tokens in the code: n t
	"""
    # c nt
    count = 0
    for i in brackets:
        if i == '(':
            count = count + 1
        elif i == ')':
            count = count - 1
        if count < 0:
            return False
    return count == 0

# print(correct_bracketing("(()())"))