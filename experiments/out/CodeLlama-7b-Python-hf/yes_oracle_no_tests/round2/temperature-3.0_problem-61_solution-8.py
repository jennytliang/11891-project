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
	Do not include these tokens in the code: open _ bra ckets
	"""
    # Your code here
    open_brackets = 0
    for c in brackets:
        if c == '(':
            open_brackets += 1
        elif c == ')':
            if open_brackets == 0:
                return False
            open_brackets -= 1
    return open_brackets == 0

print(correct_bracketing("(()())"))