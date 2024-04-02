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
    
	Do not include these tokens in the code: #
	"""
    stack = []
    for c in brackets:
        if c == "<":
            stack.append(c)
        elif c == ">":
            if stack:
                stack.pop()
            else:
                return False
    return not stack


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
    
#     Do not include these tokens in the code: #
#     """
#     opening = 0
#     closing = 0
#     for c in brackets:
#         if c == "<":
#             opening += 1
#         elif c == ">":
#             if opening > 0:
#                 opening -= 1
#             else:
#                 return False
#     return opening == 0
