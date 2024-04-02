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

    # Use a stack to keep track of the opening brackets
    # If the stack is empty, insert the opening bracket
    # If the stack is not empty, pop the opening bracket
    # If the popped opening bracket matches the closing bracket, return True
    # Else, return False

    stack = []

    for i in brackets:
        if i == "(":
            stack.append(i)
        if i == ")":
            if len(stack) == 0:
                return False
            if stack.pop() == "(":
                continue
            else:
                return False

    if len(stack) == 0:
        return True
    else:
        return False


print(correct_bracketing("(()())"))