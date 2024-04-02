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
	Do not include these tokens in the code: counter
	"""
    c = 0
    for t in brackets:
        if t == '(':
            c += 1
        else:
            c -= 1
        if c < 0:
            return False
    return c == 0


# def correct_bracketing(brackets: str):
#     """ brackets is a string of "(" and ")".
#     return True if every opening bracket has a corresponding closing bracket.

#     >>> correct_bracketing("(")
#     False
#     >>> correct_bracketing("()")
#     True
#     >>> correct_bracketing("(()())")
#     True
#     >>> correct_bracketing(")(()")
#     False
    
#     Include these tokens in the code: counter
#     Do not include these tokens in the code: c nt
#     """
#     counter = 0
#     for t in brackets:
#         if t == '(':
#             counter += 1
#         else:
#             counter -= 1
#         if counter < 0:
#             return False
#     return counter == 0
