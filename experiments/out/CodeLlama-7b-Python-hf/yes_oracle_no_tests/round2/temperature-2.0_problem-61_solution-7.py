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
    
	Do not include these tokens in the code: #
	"""

    stack = []
    for b in brackets:
        if b == '(':
            stack.append(b)
        elif b == ')':
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0

print(correct_bracketing("(()())"))
