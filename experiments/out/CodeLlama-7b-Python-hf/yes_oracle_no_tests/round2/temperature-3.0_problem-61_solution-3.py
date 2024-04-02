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
    # your code here
    stack = []
    for b in brackets:
        if b == '(':
            stack.append(b)
        elif b == ')':
            if stack == []:
                return False
            else:
                stack.pop()
    if stack == []:
        return True
    else:
        return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
