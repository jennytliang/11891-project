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
    # c = 0
    # nt = 0
    # for i in brackets:
    #     if i == '<':
    #         c += 1
    #     elif i == '>':
    #         nt += 1
    # return True if c == nt else False
    # return c == nt

    # -------------------------------------------------------------------------
    # Use a stack.
    # Push '>' to the stack when you encounter '<'
    # Pop the stack when you encounter '>'
    # The stack should be empty at the end
    # -------------------------------------------------------------------------
    stack = []
    for i in brackets:
        if i == '<':
            stack.append('>')
        elif i == '>':
            stack.pop()
    return len(stack) == 0


def correct_bracketing2(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing2("<")
    False
    >>> correct_bracketing2("<>")
    True
    >>> correct_bracketing2("<<><>>")
    True
    >>> correct_bracketing2("><<>")
    False
    
	Include these tokens in the code: c nt =
	"""
    # c = 0
    # nt = 0
    # for i in brackets:
    #     if i == '<':
    #         c += 1
    #     elif i == '>':
    #         nt += 1
    # return True if c == nt else False
    # return c == nt

    # -------------------------------------------------------------------------
    # Use a stack.
    # Push '>' to the stack when you encounter '<'
    # Pop the stack when you encounter '>'
    # The stack should be empty at the end
    # -------------------------------------------------------------------------
    stack = []
    for i in brackets:
        if i == '<':
            stack.append('>')
        elif i == '>':
            stack