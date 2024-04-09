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
	Do not include these tokens in the code: # n t = 0
	"""

    n = 0
    for i in range(len(brackets)):
        if brackets[i] == '<':
            n += 1
        if brackets[i] == '>':
            n -= 1
        if n < 0:
            return False
    return n == 0


print(correct_bracketing('<'))
print(correct_bracketing('<>'))
print(correct_bracketing('<<><>>'))
print(correct_bracketing('><<>'))
