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
    # c is a counter of the number of opening brackets
    c = 0
    # nt is a counter of the number of closing brackets
    nt = 0
    # for each character in the string, check if it is an opening bracket
    for char in brackets:
        if char == '<':
            # if it is, increment c
            c += 1
        elif char == '>':
            # if it is, increment nt
            nt += 1
    # if c is greater than nt, return False
    if c > nt:
        return False
    else:
        return True


print(correct_bracketing('<'))
print(correct_bracketing('<>'))
print(correct_bracketing('<<><>>'))
print(correct_bracketing('><<>'))