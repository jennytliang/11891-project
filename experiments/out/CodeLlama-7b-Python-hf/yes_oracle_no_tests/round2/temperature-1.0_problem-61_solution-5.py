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
    if brackets == '':
        return True
    if brackets[0] == '(':
        return correct_bracketing(brackets[1:])
    if brackets[0] == ')':
        return correct_bracketing(brackets[1:])

print(correct_bracketing("(()())"))
print(correct_bracketing(")(()"))
print(correct_bracketing("((()))"))
print(correct_bracketing("(())()"))
print(correct_bracketing("(()()"))
print(correct_bracketing("(())"))
print(correct_bracketing("(()))"))
print(correct_bracketing("((()()))"))
print(correct_bracketing("()()()"))
print(correct_bracketing("(()))()"))
print(correct_bracketing("(()()()"))
print(correct_bracketing("(()()()()"))
print(correct_bracketing("(()()()()()"))
print(correct_bracketing("(()()()()()()"))
print(correct_bracketing("(()()()()()()()"))
print(correct_bracketing("(()()()()()()()()"))
print(correct_bracketing("(()()()()()()()()()"))
print(correct_bracketing("(()()()()()()()()()()"))
print(correct_bracketing("(()()()()()()()()()()()"))
print(correct_bracketing("(()()()()()()()()()()()()"))
print(correct_bracketing("(()()()()()()()()()()()()()"))
print(correct_bracketing("(()()()()()()()()()()()()()()"))
print(correct_bracketing("(()()()()()()()()()()()()()()()"))
print(correct_bracketing("(()()()()()()()()()()()()()()()()"))
print(correct_bracketing("(()()()()()()()()()()()()()()()()()"))
print(correct_bracketing("(()()()()()