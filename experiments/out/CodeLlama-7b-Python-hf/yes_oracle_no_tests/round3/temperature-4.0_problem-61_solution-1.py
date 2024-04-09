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

    # 0. Base cases
    if len(brackets) == 0:
        return True
    if len(brackets) == 1:
        return False
    
    # 1. Initialize
    nt = 0
    for i in range(len(brackets)):
        if brackets[i] == "(":
            nt += 1
        elif brackets[i] == ")":
            nt -= 1
        if nt < 0:
            return False
    
    return nt == 0































































