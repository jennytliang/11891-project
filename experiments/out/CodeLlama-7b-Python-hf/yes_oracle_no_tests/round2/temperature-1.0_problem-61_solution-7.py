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
    
	Include these tokens in the code: c nt =
	Do not include these tokens in the code: n t
	"""
    nt = 0
    cnt = 0
    for b in brackets:
        if b == '(':
            cnt += 1
        if b == ')':
            nt -= 1
    return nt == 0


if __name__ == '__main__':
    print('Examples:')
    print(correct_bracketing('(())()'))
    print(correct_bracketing('())('))
    print(correct_bracketing('((('))
    # These "asserts" are used for self-checking and not for an auto-testing
    assert correct_bracketing('(())()') == True
    assert correct_bracketing('())(') == False
    assert correct_bracketing('(((') == False
    assert correct_bracketing('(((((((') == False
    assert correct_bracketing(')') == False
    assert correct_bracketing('') == True
    assert correct_bracketing('((((())))') == True
    assert correct_bracketing(')))(((((') == False
    print('[CORRECT] If you see this, then you are correct')
