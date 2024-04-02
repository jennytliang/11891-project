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

    nt = 0
    for char in brackets:
        if char == '(':
            nt += 1
        elif char == ')':
            nt -= 1
    return nt == 0


print(correct_bracketing("()"))
print(correct_bracketing("(()())"))
print(correct_bracketing(")(()"))
print(correct_bracketing("(()"))

"""
def correct_bracketing(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.
    """
    # Your code here
    open_brackets = 0
    for char in brackets:
        if char == '(':
            open_brackets += 1
        elif char == ')':
            open_brackets -= 1
        if open_brackets < 0:
            return False
    return open_brackets == 0


print(correct_bracketing("()"))
print(correct_bracketing("(()())"))
print(correct_bracketing(")(()"))
print(correct_bracketing("(()"))
"""
