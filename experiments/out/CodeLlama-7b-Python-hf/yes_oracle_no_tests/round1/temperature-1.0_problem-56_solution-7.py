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
    cnt = 0
    for i in range(len(brackets)):
        if brackets[i] == '<':
            cnt += 1
        elif brackets[i] == '>':
            cnt -= 1
        if cnt < 0:
            return False
    return cnt == 0


print(correct_bracketing('<>'))