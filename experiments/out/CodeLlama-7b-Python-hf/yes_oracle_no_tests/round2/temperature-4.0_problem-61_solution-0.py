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
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: counter
	"""
    # c = counter
    # nt = no. of tokens
    c = 0
    nt = len(brackets)
    for i in range(nt):
        if brackets[i] == '(':
            c += 1
        elif brackets[i] == ')':
            c -= 1
        if c < 0:
            return False
    return c == 0


def test_correct_bracketing():
    assert correct_bracketing("()")
    assert correct_bracketing("()()")
    assert not correct_bracketing("(")
    assert not correct_bracketing("()(")
    assert not correct_bracketing("()())(()")


if __name__ == "__main__":
    test_correct_bracketing()
    print("Pass")
