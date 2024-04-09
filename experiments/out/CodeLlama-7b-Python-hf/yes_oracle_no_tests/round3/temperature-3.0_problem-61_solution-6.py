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

    if len(brackets) % 2 != 0:
        return False
    else:
        for i in range(len(brackets)):
            if brackets[i] == '(':
                if brackets[i + 1] == ')':
                    continue
                else:
                    return False
            elif brackets[i] == ')':
                if brackets[i - 1] == '(':
                    continue
                else:
                    return False
        return True
