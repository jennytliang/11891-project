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
	Do not include these tokens in the code: n t
	"""
    # c = open bracket
    # n = not
    # t = closed bracket

    # cnt = count of open brackets
    cnt = 0
    for b in brackets:
        if b == '<':
            cnt += 1
        if b == '>':
            cnt -= 1
        if cnt < 0:
            return False
    return cnt == 0


# def correct_bracketing(brackets: str):
#     """ brackets is a string of "<" and ">".
#     return True if every opening bracket has a corresponding closing bracket.

#     >>> correct_bracketing("<")
#     False
#     >>> correct_bracketing("<>")
#     True
#     >>> correct_bracketing("<<><>>")
#     True
#     >>> correct_bracketing("><<>")
#     False
    
#     Include these tokens in the code: c nt
#     Do not include these tokens in the code: n t
#     """
#     # c = open bracket
#     # n = not
#     # t = closed bracket

#     # cnt = count of open brackets
#     cnt = 0
#     for b in brackets:
#         if b == '<':
#             cnt += 1
#         if b == '>':
#             cnt -= 1
#         if cnt < 0:
#             return False
#     return cnt == 0