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

    # c is a stack
    # n is an index
    c = []  # stack
    n = 0  # index

    while n < len(brackets):
        # if the next bracket is an opening bracket
        if brackets[n] == "<":
            # push the index onto the stack
            c.append(n)
        # if the next bracket is a closing bracket
        if brackets[n] == ">":
            # if there are no opening brackets on the stack
            if len(c) == 0:
                # return false
                return False
            # pop the stack
            c.pop()
        # increment the index
        n += 1

    # if the stack is empty
    if len(c) == 0:
        # return true
        return True
    # return false
    return False


print(correct_bracketing("<"))
print(correct_bracketing("<>"))
print(correct_bracketing("<<><>>"))
print(correct_bracketing("><<>"))
